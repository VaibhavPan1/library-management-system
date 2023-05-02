from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image

def about():
    root = Tk()
    root.title("About")
    root.geometry("823x400")


    frame = Frame(root,bg='light grey')
    frame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

    label1 = Label(frame, text = "Library Management System", font="Cambria 15")
    label1.place(relx=0.09, rely=0.09,relwidth=0.8,relheight=0.1)

    label2 = Label(frame, text="This is a simple Library Management System developed by Vaibhav Kumar Pandey. A students of United College Of Engineering And Research, Naini, Prayagraj, pursuing BTech in the field of Computer Science.\nThis project is written is Python Language and utilizes database connectivity using MySQL.\n All the essential features that are necessary in a LMS are added in this project. ")
    label2.place(relx=0.09, rely=0.2)

    root.mainloop()

