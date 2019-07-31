# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:01:11 2019

@author: ACER PC
"""
#-----------header---------------
from tkinter import *
import os
from tkinter.filedialog import *
window = Tk()
window.title('textbox')

frame = Frame(window, background='sky blue', borderwidth=1)
frame.pack()

window.title(os.path.asename(in_path)+ ' -myNote' )

#-----------Text box and scrollbar----------------------------
textbox = Text(frame, height=26 , width=50)
textbox.pack(side=LEFT, expand=YES, fill=BOTH)

scrollbar = Scrollbar(frame, borderwidth=5, orient=VERTICAL,command=textbox.yview)
scrollbar.pack(side=RIGHT, fill=BOTH)

textbox.configure(yscrollcommand=scrollbar.set)

#---------menuBar functions----------------------
def newPage():
	pass

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


	def cut():
		pass

	def Copy():
		pass

	def Paste():
		pass

	def delete():
		pass

	def find():
		pass

	def find_next():
		pass

	def replace():
		pass

	def go_to():
		pass

	def select_all():
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
fileMenu.add_command(label='Page setup', command= newPage)
fileMenu.add_command(label='Print', command=newPage)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=exit)
menubar.add_cascade(label='File', menu=fileMenu, underline=0)
window.config(menu = menubar)

#create file and its submenus
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label='Cut           ctrl x', command=newPage)
fileMenu.add_command(label='Copy          ctrl c', command=newPage)
fileMenu.add_command(label='Paste         ctrl v', command=newPage)
fileMenu.add_command(label='Delete        ctrl d', command=newPage)
fileMenu.add_separator()
fileMenu.add_command(label='Find...', command= newPage)
fileMenu.add_command(label='Find Next', command=newPage)
fileMenu.add_command(label='Replace...', command=newPage)
fileMenu.add_command(label='Go To...', command=newPage)
fileMenu.add_separator()
fileMenu.add_command(label='Select All', command=newPage)
fileMenu.add_command(label='Time/Date', command=newPage)
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