import socket

ip=str(input("the ip which you want to connect:"))
HOST=ip
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
        cmd=input("Please input cmd:")      #与人交互，输入命令
        s.sendall(bytes(cmd,'utf-8'))      #把命令发送给对端
        data=s.recv(1024)     #把接收的数据定义为变量
        print(data)#输出变量
        if cmd=='close':
            break;
s.close()   #关闭连接