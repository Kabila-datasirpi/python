from tkinter import *

def func1():
    label3=Label(window,text=entry1.get())
    label3.grid(row=5,column=3)

window=Tk()  #to create a GUI window
window.title("Hotel Management System")  #to show title name
window.geometry("600x600")  #to fix the window size screen

label1=Label(window,text="Welcome to our Hotel",foreground="Red")
label1.grid(row=1,column=1)

label2=Label(window,text="First name")
label2.grid(row=2,column=2)

entry1=Entry(window,text="")
entry1.grid(row=2,column=3)

button1=Button(window,text="Submit",command=func1)
button1.grid(row=4,column=3)

