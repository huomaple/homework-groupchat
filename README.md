# homework-groupchat
用python编写多人群聊用的客户端以及服务端

## 运行环境
- 服务端：CentOS7.0
- 客户端：windows
- python版本：3.6.0

## 运行的GIF图
![](https://github.com/huomaple/homework-groupchat/blob/master/01.gif)
![](https://github.com/huomaple/homework-groupchat/blob/master/02.gif)
## 流程以及目的
- 本次作业采用python的socket套接字的tcp模式进行数据之间的传递，多人群聊的原理是每当有人登陆服务端时便会产生一个子进程进行管理，然后在主进程里面建立一个list管理这些子进程，有人发出聊天信息的时候便会将发送list里面除了本人之外的其他人。而list里面人员的退出则是采用定时向客户端发送一个包，若在一定时间里面没有回应的话则会将这个子进程以及list中的信息移除出去。
- 表情包则是使用了wxpython中的richtext中的RichTextCtrl控件进行实现，该控件中有addImage的函数可以将图片信息发送到控件里面，但是该控件有一个不足之处就是图片发送到控件里面但是无法进行操作，即里面有图片但不能用其控件下的GetValue函数进行获取，也无法对其进行复制或者黏贴。所以，这里的解决办法就是使用正则表达式进行图片与文字之间的转化，当点击表情时会加载一个[xx]的文字进入到控件里面，xx是代表了图片的编号，当你输出之后，会用一个正则匹配将[xx]里面的数据转化成为图片。但这个方法也有一个缺点就是文字和表情包无法连接在同一行上，因为两者采用了不同的输入方式进行输入的。这里是本人水平不足导致的，这个地方之后会进行优化的。
- 文件的传送则是将文件先用二进制进行读取，分段地将文件一段一段进行发送，发送前后用md5进行校验，如果md5校验结果相等就是发送成功，否则就是发送失败。这个分段的方法比较简单易懂，但是传送的效率很慢，基本上只能传送1MB以下的东西，而且如果分段发送的次数过于频繁则会产生粘包的现象，即是两个包的数据会复合到一个包里面，另一个包则会有部分数据丢失。
## 实验总结
- 通过这次编写代码基本上是用了一下socket套接字的用法和对wxpython这个库的基础用法，最大收获就是这次GUI的设计和表情包的输入基本上是对着wxpython的源代码进行编写的，对整个流程都比较熟悉了。但这次的成果只能说是能够跑起来，其中掺杂着成吨的bug和出错没有进行处理，还有wxpython本身的不足，所以这之后还需要对这个程序进行改良和修正。
