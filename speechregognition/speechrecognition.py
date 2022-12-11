from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk,Image
import threading
import speech

def get_image(filename,width,height):
    imagine=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(imagine)

top=Tk()
top.title("语音开启电风扇")
top.geometry('1000x500')
canvas_top =Canvas(top,width=1000,height=500)
back=get_image('D:\\桌面\\voice.jpg',1000,500)
canvas_top.create_image(500,250,image=back)
canvas_top.pack()
v = StringVar()
v.set('1')

def start_thread():
    thread = threading.Thread(target=open_speech_recognize, args=())
    thread.setDaemon(True)
    thread.start()

def open_speech_recognize():
    i=0
    speech.say("请点击麦克风按钮并说风扇或关闭或退出")
    while TRUE:
        i=i+1
        if i==7:
            speech.say("输入次数过多，暂停语音识别")
            sys.exit()
        response = speech.input()
        if response=="风扇":
            speech.say("正在打开风扇")
        else:
            if response=="关闭":
                speech.say("正在关闭风扇")
            else:
                if response=="退出":
                    speech.say("正在结束程序")
                    top.destroy()
                else:
                    speech.say("我听到的是"+response+",不太符合要求")

def on_Click():
    speech.say("正在关闭界面")
    top.destroy()

def click_event():
    speech.say("正在"+v.get()+"风扇")
    ck['text'] = v.get()

lab = Label(top, text='风扇当前状态：', font='宋体 -16')
lab.pack()
lab.place(x=380,y=100,width=150,height=35)
 
ck = Checkbutton(top, variable=v, text='关闭', font='宋体 -18',
                    onvalue='打开', offvalue='关闭',
                    command=click_event)
ck.pack()
ck.place(x=530,y=100,width=100,height=35)

label=Label(top,text="请点击按钮或开关打开或关闭风扇")
button1=Button(top,text="点击开始语音识别",fg="tomato",compound=CENTER,command=start_thread)
button2=Button(top,text="关闭界面",fg="tomato",compound=CENTER,command=on_Click)
label.pack()
label.place(x=400,y=20,width=200,height=20)
button1.pack()
button1.place(x=450,y=55,width=100,height=30)
button2.pack()
button2.place(x=460,y=140,width=80,height=30)

top.mainloop()
