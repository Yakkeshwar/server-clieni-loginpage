import socket
import tkinter as tk
import tkinter.ttk as ttk
import getpass
from tkinter import E,W
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
import random
import os
import pickle

s=socket.socket()
port=7777

s.connect(('ip address',port))

window=tk.Tk()

window.title('HOME PROJECT')
window.geometry('500x350')

lbl3=tk.Label(window,text="Welcome to PlasmaTech's Login Page",font=('Comic San MS',10))
lbl3.grid(column=0,row=0,padx=5,pady=5)
lbl1=tk.Label(window,text='UserName: ',font=('Comic San MS',10))
lbl1.grid(column=0,row=1,sticky=E,padx=5,pady=5)
lbl2=tk.Label(window,text='Password: ',font=('Comic San MS',10))
lbl2.grid(column=0,row=2,sticky=E,padx=5,pady=5)

txt1=tk.Entry(window,width=20)
txt1.grid(column=1,row=1)
txt2=tk.Entry(window,width=20,show='*')
txt2.grid(column=1,row=2)


def login():
    sendinfo='1'
    username=txt1.get()
    password=txt2.get()
    array=[sendinfo,username,password]
    data=pickle.dumps(array)
    s.send(data)
    FlagStat=s.recv(1024).decode()
    if(FlagStat=='1'):
        login=tk.Tk()
    elif(FlagStat=='0'):
        messagebox.showerror('ERROR','USERNAME OR PASSWORD INCORRECT')

btn1=tk.Button(window,text='Create A New Account')#"""command=new"""
btn1.grid(column=1,row=4,columnspan=10,sticky=W)
btn2=tk.Button(window,text='Log In',command=login)
btn2.grid(column=1,row=3,sticky=W,pady=5)
btn3=tk.Button(window,text='Forgot Password')#"""command=forgot"""
btn3.grid(column=2,row=3,sticky=W,pady=5)

window.mainloop()
