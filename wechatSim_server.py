# -*- coding : utf-8 -*-
import socket
import threading
import socketserver
import select
import os
import time
import hashlib
import struct

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        name = self.request.recv(buffersize)
        name = name.decode(encoding = 'utf-8')
        loginlist[name] = self.request
        olPL.append(name)
        #print(loginlist)
        #print(olPL)
        cur_thread = threading.current_thread()
        while 1:
            try:
                data = self.request.recv(buffersize)
                #print(loginlist)
                for i in loginlist.items():
                    if i[0] != name:
                        send_name = name
                        i[1].sendall(send_name.encode(encoding = 'utf-8'))
                        i[1].sendall(data)
            except Exception as e :
                loginlist.pop(name)
                olPL.remove(name)
                #print(loginlist)
                #print(olPL)
                break

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):#继承ThreadingMixIn表示使用多线程处理request，注意这两个类的继承顺序不能变
    pass


class FileTCP(socketserver.BaseRequestHandler):
    
    BUFFER_SIZE = 1024
    HEAD_STRUCT = '128sIq32s'
    info_size = struct.calcsize(HEAD_STRUCT)

    def handle(self):
        type = self.request.recv(1)
        #print(type)
        if type.decode(encoding = 'utf-8') == '0':
            filename = self.request.recv(FileTCP.BUFFER_SIZE)
            filename = filename.decode(encoding = 'utf-8')
            file_path = r'/home/python/FileDownLoad/' + filename
            self.send_file(file_path)
        else:
            self.recv_file()
        
    def cal_md5(file_path):
        with open(file_path, 'rb') as fr:
            md5 = hashlib.md5()
            md5.update(fr.read())
            md5 = md5.hexdigest()
        return md5

    def get_file_info(file_path):
        #print(file_path)
        file_name = os.path.basename(file_path)
        file_name_len = len(file_name)
        file_size = os.path.getsize(file_path)
        md5 = FileTCP.cal_md5(file_path)
        return file_name, file_name_len, file_size, md5


    def send_file(self, file_path):
        file_name, file_name_len, file_size, md5 = FileTCP.get_file_info(file_path)
        file_head = struct.pack(FileTCP.HEAD_STRUCT, file_name.encode(encoding = 'utf-8'), file_name_len, file_size, md5.encode(encoding = 'utf-8'))

        try:
            self.request.sendall(file_head)
            sent_size = 0

            with open(file_path , 'rb') as fr:
                while sent_size < file_size:
                    remained_size = file_size - sent_size
                    send_size = 0
                    if remained_size > FileTCP.BUFFER_SIZE :
                        send_size = FileTCP.BUFFER_SIZE
                    else :
                        send_size = remained_size
                    send_file = fr.read(send_size)
                    sent_size += send_size
                    self.request.sendall(send_file)
                    time.sleep(0.2)
        except Exception as e:
            pass
        finally:
            self.request.close()

    
    def unpack_file_info(file_info):
        file_name, file_name_len, file_size, md5 = struct.unpack(FileTCP.HEAD_STRUCT, file_info)
        file_name = file_name.decode(encoding = 'utf-8')
        md5 = md5.decode(encoding = 'utf-8')
        file_name = file_name[:file_name_len]
        return file_name, file_size, md5


    def recv_file(self ):
        file_info_package = self.request.recv(FileTCP.info_size)
        #print(file_info_package)
        file_name, file_size, md5_recv = FileTCP.unpack_file_info(file_info_package)
        #print('filename',file_name)
        #print('filesize',file_size)

        recved_size = 0
        with open(r'/home/python/FileDownLoad/'+file_name, 'wb') as fw:
            while recved_size < file_size:
                remained_size = file_size - recved_size
                recv_size = 0
                if remained_size > FileTCP.BUFFER_SIZE :
                    recv_size = FileTCP.BUFFER_SIZE 
                else :
                    recv_size = remained_size
                recv_file = self.request.recv(recv_size)
                recved_size += recv_size
                fw.write(recv_file)
        md5 = FileTCP.cal_md5(r'/home/python/FileDownLoad/'+file_name)
        if md5 != md5_recv:
            self.request.sendall('0'.encode(encoding='utf-8'))
        else:
            self.request.sendall('1'.encode(encoding='utf-8'))
        self.request.close()


    
        
class MyServer(socketserver.BaseRequestHandler):  # 创建一个类，继承自socketserver模块下的BaseRequestHandler类
    def handle(self):  # 要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）
        name = ''
        while 1:
            try:
                send_data = ''
                conn = self.request
                addr = self.client_address
                readable = select.select([conn], [], [], 10)
                if readable[0] == []: 
                    break    
                rec_data = conn.recv(2048)
                name = rec_data.decode(encoding = 'utf-8')
                for i in olPL:
                    send_data = send_data + i + '\n'
                conn.sendall(send_data.encode(encoding='utf-8'))

                time.sleep(1)
                fnamelist = os.listdir(r'/home/python/FileDownLoad')

                file_send_data = ''
                for i in fnamelist:
                    file_send_data = file_send_data + i + '\n'
                conn.sendall( file_send_data.encode( encoding = 'utf-8' ) )

                conn.close()
            except Exception as e:
                break
        #loginlist.pop(name)
        #olPL.remove(name)
        #print(loginlist)
        #print(olPL)


if __name__ == "__main__":
    

    HOST = ""
    PORT = 23334
    buffersize = 1024
    addr = (HOST, PORT)
    server = ThreadedTCPServer(addr, ThreadedTCPRequestHandler)
    ip, port = server.server_address
    loginlist = {}
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    FHOST = ""
    FPORT = 23336
    Fbuffersize = 1024
    Faddr = (FHOST , FPORT)
    Fserver = ThreadedTCPServer(Faddr , FileTCP)
    Fserver_Thread = threading.Thread(target = Fserver.serve_forever )
    Fserver_Thread.daemon = True
    Fserver_Thread.start()

    while 1:
        olPL = ['---在线人员---']
        sever = socketserver.ThreadingTCPServer(("", 23335),MyServer)  # 传入端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象
        sever.serve_forever()
        pass