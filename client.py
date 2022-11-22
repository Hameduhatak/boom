import base64
from platform import uname
import threading
import socket
import time , datetime
from Tkinter import *


def speed():
    def check():
        na = False
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sec1 = datetime.datetime.now()
        try:
            ipp = socket.gethostbyname("google.com")
            s.connect((ipp,80))
        except Exception as e:
            secened = e
            na = True
        sec2 = datetime.datetime.now()
        sec3 = sec2 - sec1
        if na == False:
            sa =int(sec3.total_seconds() * 1000)
            secened = str(sa)+"mili sec"
        label = Label(rooot , text=secened,bg="green")
        label.pack(side=TOP , fill=X)
        s.close()
    #c

    rooot = Tk()
    button1 = Button(rooot, text="Check !" , command=check).pack(fill=X , side=BOTTOM)
    rooot.mainloop()
def start_speed():
    threading.Thread(target=speed).start()


def asl():
    try:
        ip = "88.99.86.239"
        client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
        client.connect((ip ,5002))
    except Exception as e:
        rooot = Tk()
        label = Label(rooot , text=e)
        label.pack(side=TOP , fill=X)
        rooot.mainloop()
        exit()
    name = uname()[1]; #:)))

    root = Tk()
    canvas = Canvas(root)
    scrollbar = Scrollbar(root , orient="vertical" , command=canvas.yview)
    frame = Frame(canvas)
    if name == "":
        exit()
    def send():
    
        data_send = edit_Text.get()
        if data_send != "":
            label = Label(frame , text='~~~~~~~~~~~~~~~~~~~~~' , bg="red" , fg="white")
            label.pack(side=TOP , fill=X)
            aa = name+" : "+data_send
            client.send(aa.encode())
            label = Label(frame , text='~~~~~~~~~~~~~~~~~~~~~' , bg="green" , fg="white")
            label.pack(side=TOP , fill=X)
        #label = Label(frame , text=data_send , bg="red" , fg="white")
        #label.pack(side=TOP , fill=X)
            edit_Text.delete(0 , END)



    def recv():
        while True:
            data_recv = client.recv(60)
            label = Label(frame , text=(data_recv) , bg="black" , fg="white")
            label.pack(side=TOP , fill=X)


    def update():
        while True:
            canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
            time.sleep(2)


#button11 = Button(root , text="speed test !" , command=start_speed,height=1,width=10)
#button11.pack( side=TOP,anchor=NW)
#button12 = Button(root , text="UDP Client" , command=start_speed,height=1,width=10)
#button12.pack( side=TOP,anchor=NW)
    button = Button(root , text="Send" , command=send)
    edit_Text = Entry(root)



    button.pack(fill=X , side=BOTTOM)
    edit_Text.pack(fill=X , side=BOTTOM)

    canvas.pack(fill="both" , side="left" ,  expand=True)
    scrollbar.pack(fill="y" , side="right")
    canvas.create_window(0,0,anchor='nw', window=frame)
    canvas.update_idletasks()


    threading.Thread(target=recv).start()
    threading.Thread(target=update).start()

    root.geometry("500x600")
    root.title("Client")
    root.resizable(width=True , height=True)


    root.mainloop()

def udp():
    UDPsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    adrr = ("127.0.0.1",1700)
    ud = Tk()
    def sendd():
    
        data_send = text.get()
        if data_send != "":
            try:
                UDPsock.sendto(data_send.encode(),adrr)
            except Exception as err:
                label = Label(ud , text=err , bg="red" , fg="white")
                label.pack(side=TOP , fill=X)
            label = Label(ud , text="Send ~" , bg="green" , fg="white")
            label.pack(side=TOP , fill=X)
            text.delete(0 , END)
    text = Entry(ud)
    text.pack(fill=X , side=BOTTOM)
    Button(ud, text="send !" , command=sendd).pack(fill=X,side=TOP)
    ud.title("UDP")
    ud.resizable(width=True,height=True)
    ud.mainloop()

r__t = Tk()
def T_asl():
    threading.Thread(target=asl).start()
def T_udp():
    threading.Thread(target=udp).start()
Button(r__t , text="TCP Client !" , command=T_asl).pack(fill=X,side=TOP)
Button(r__t , text="Speed test" , command=start_speed).pack(fill=X,side=TOP)
Button(r__t , text="UDP Client" , command=T_udp).pack(fill=X,side=TOP)
r__t.geometry("250x250")
r__t.title("Client")
r__t.resizable(width=True , height=True)
r__t.mainloop()
