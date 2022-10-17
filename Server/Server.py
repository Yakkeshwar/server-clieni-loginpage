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
print('Socket successfully created')

port=7777

s.bind(('',port))
print('Bound successfully to port: ',port)

s.listen(2)
print('Socket Listening.....')

while True:
    c,addr=s.accept()
    print('Got connection from address: ', addr )
    option=c.recv(2048)
    option1=pickle.loads(option)
    if ( option1[0] == '1' ):
        flag=0
        fread=open('CustomerRecords.log','r')
        readwhole=fread.read()
        count_records=readwhole.count('\n')
        fread.seek(0,0)
        for count1 in range (0,count_records,1):
            read_line=fread.readline()
            seperated_line=read_line.split(';')
            if(seperated_line[0]==option1[1] and seperated_line[2]==option1[2]):
                flag=1
            else:
                flag=0
        c.send(str(flag).encode())
            
