# this was one of the learning projects
# i've found useful for understanding concepts of changing models
# and for understanding Morse Code itself
# NB-NOTE: THE ORIGINAL PROJECT
# CAN BE FOUND IN THE FOLLOWING ADDRESS:
# https://www.geeksforgeeks.org/morse-code-translator-python


# This Project is redesigned and updated in a more understandable way
# by me! (/https://github.com/AmirHosseinRnj1)
# If you have any problem running or understanding this project,
# feel free to make contact with me...



# TKINTER MODULE SETUP

#import tkinter module and some UIs
from tkinter import *
import random,datetime,time
from tkinter import Label
from Morse import *

####################
### creating GUI ###
####################

# creating root object
root = Tk()
# defining size of the window
root.geometry("1200x2000")
# defining title
root.title("Morse <> English ")

# creating frames
f1 = Frame(root,width=1600,relief=SUNKEN)
f1.pack(side=TOP)

f2 = Frame(root,width=2000,height=1000,relief=SUNKEN)
f2.pack(side=TOP)

f3 = Frame(root,width=1000,relief=SUNKEN)
f3.pack(side=BOTTOM)

localtime = time.asctime(time.localtime(time.time()))

# initialize parameters
enc = StringVar()
dec = StringVar()
txt = StringVar()
submit = StringVar()
result = StringVar()

def exit():
    root.destroy()

def reShow():
    if btnEnc and btnSub:
        result.set(encrypt(txt))
    elif btnDec and btnSub:
        result.set(decrypt(txt))

lblInfo = Label(f1,font=('helvetica',50,'bold'),
                text="Morse <=> txt",
                fg='Steel Blue',bd=10,anchor="w")
lblInfo.grid(row=0,column=0)

lblInfo = Label(f1,font=('helvetica',50,'bold'),
                text=f"your Local time is: {localtime}",
                fg='Steel Blue',bd=10,anchor="w")
lblInfo.grid(row=1,column=0)

btnEnc = Button(f2,padx=16,pady=8,bd=16,fg="black",
                font=('Arial', 16, 'bold'), width=10,
                text="Encode", bg="powder blue").grid(row=0, column=0)

btnDec = Button(f2,padx=16,pady=8,bd=16,fg="black",
                 font=('Arial',16,'bold'),width=10,
                 text="Decrypt",bg="powder blue").grid(row=1,column=0)

txtMode = Entry(f2,font=('arial',16,'bold'),
               textvariable=txt,bd=10,insertwidth=4,
               bg="Powder Blue",justify="center")
txtMode.grid(row=1,column=1)

btnSub = Button(f2,padx=16,pady=8,bd=16,fg="black",
                 font=('Arial',16,'bold'),width=10,
                 text="Show Result",bg="powder blue",
                 command=reShow).grid(row=1,column=2)

txtService = Entry(f3,font=('arial',16,'bold'),
               textvariable=result,bd=10,insertwidth=4,
               bg="Powder Blue",justify="center")
txtService.grid(row=1,column=1)

root.mainloop()