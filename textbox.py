# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:01:11 2019

@author: ACER PC
"""
#-----------header---------------
from tkinter import *
import os
from tkinter.filedialog import *
import time;
window = Tk()
window.title('textbox')
in_path = ''
frame = Frame(window, background='sky blue', borderwidth=1)
frame.pack()

window.title(os.path.basename(in_path)+ ' -myNote' )

#-----------Text box and scrollbar----------------------------
textbox = Text(frame,height = 42, width = 168,)
textbox.pack(side=LEFT, expand=YES, fill=BOTH)

scrollbar = Scrollbar(frame, borderwidth=5, orient=VERTICAL,command=textbox.yview)
scrollbar.pack(side=RIGHT, fill=BOTH)

textbox.configure(yscrollcommand=scrollbar.set)

#---------menuBar functions----------------------
def getColor():
    color = askcolor()
def newPage():
    global fileName
    root.title('Untitled Mynote')
    fileName = None
    textbox.delete(1.0,'end')
	

def open_file():
    fileName = askopenfilename(filetypes=[('Text files', '.txt')])
    s = open(fileName).read()
    textbox.insert(END, s)

def save_as():
	fileName = asksaveasfilename(filetypes=[('Text files', '.txt')])
	s = open(fileName, 'w')
	

def save_file():
	fileName = asksaveasfile(defaultextension='.txt')
	file_to_save = str(textbox.get(0.0, END))
	fileName.write(file_to_save)
	fileName.close

def exit():
	window.destroy()


def Cut():
    textbox.event_generate('<<Cut>>')
		

def Copy():
    textbox.event_generate('<<Copy>>')
		

def Paste():
    textbox.event_generate('<<Paste>>')
		
def delete():
    pass
def find():
    pass
def DateTime():
    localtime = time.asctime(time.localtime(time.time()))


def find_next():
    pass

def replace():
    pass

def go_to():
    pass

def select_all():
    pass


def timeNdate():
    pass

def word_map():
    pass

def font():
    pass

def status_bar():
    pass

def view():
    pass

def help():
    pass

def about():
    pass

def notepad():
    pass


#-----------------create all fileMenu optios---------------------
#create all menubar objects
menubar = Menu(window)

#create file and its submenus
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label='New                Ctrl+N', command=newPage)
fileMenu.add_command(label='Open...            Ctrl+O', command=open_file)
fileMenu.add_command(label='save               ctrl S', command=save_file)
fileMenu.add_command(label='save As...   crtl+shift+s', command=save_as)
fileMenu.add_separator()
fileMenu.add_command(label='Page setup', command= newPage, accelerator = 'Ctrl+N')
fileMenu.add_command(label='Print', command=newPage)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=exit)
menubar.add_cascade(label='File', menu=fileMenu, underline=0)
window.config(menu = menubar)

#create file and its submenus
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label='Cut           Ctrl+X', command=Cut, accelerator = 'Ctrl+X')
fileMenu.add_command(label='Copy          Ctrl+C', command=Copy, accelerator = 'Ctrl+C')
fileMenu.add_command(label='Paste         Ctrl+V', command=Paste, accelerator = 'Ctrl+V')
fileMenu.add_command(label='Delete        ctrl d', command=newPage)
fileMenu.add_separator()
fileMenu.add_command(label='Find...', command= newPage)
fileMenu.add_command(label='Find Next', command=newPage)
fileMenu.add_command(label='Replace...', command=newPage)
fileMenu.add_command(label='Go To...', command=getColor)
fileMenu.add_separator()
fileMenu.add_command(label='Select All', command=newPage)
fileMenu.add_command(label='Time/Date', command=DateTime)
menubar.add_cascade(label='Edit', menu=fileMenu, underline=0)
window.config(menu = menubar)

#create file and its submenus
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label='Word Wrap', command=newPage)
fileMenu.add_command(label='Font', command=newPage)
menubar.add_cascade(label='Format', menu=fileMenu, underline=0)
window.config(menu = menubar)

#create file and its submenus
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label='Status Bar', command=newPage)
menubar.add_cascade(label='View', menu=fileMenu, underline=0)
window.config(menu = menubar)

#create file and its submenus
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label='View', command=newPage)
fileMenu.add_command(label='Help', command=newPage)
fileMenu.add_separator()
fileMenu.add_command(label='About', command=newPage)
fileMenu.add_command(label='Notepad', command=newPage)
menubar.add_cascade(label='Help', menu=fileMenu, underline=0)
window.config(menu = menubar)



window.mainloop()