from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from addBook import *
from deleteBook import *
from viewBooks import *
from issueBook import *
from returnBook import *
from About import *


mypass ="8299" #enter your database password
mydatabase = "db" #database name

con = pymysql.connect(host="localhost",user="root",password=mypass ,database=mydatabase)
#root is the user

cur = con.cursor() #cursor for executing commands

root = Tk()
root.title("Central Library")
root.minsize(width=600,height=600) #new method for minimum size
root.geometry("600x500")

background_img = Image.open("img2.jpg")
[imageSizeWidth, imageSizeHeight] = background_img.size

newImageSizeWidth = int(imageSizeWidth*0.15)
newImageSizeHeight = int(imageSizeHeight*0.22)

background_img = background_img.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)

img2= ImageTk.PhotoImage(background_img)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img2)
Canvas1.config(bg='white',width=newImageSizeWidth,height=newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="yellow",bd=2)
headingFrame1.place(relx=0.2,rely=0.08,relwidth=0.6,relheight=0.07)
headingLabel = Label(headingFrame1, text="Library Management System", bg='black', fg='white', font=('Calibri',18))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='black', fg='white',font=('Calibri'), command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete,font=('Calibri'))
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View,font=('Calibri'))
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white',command=issueBook,font=('Calibri'))
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white',command=returnBook,font=('Calibri'))
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Exit", bg='black', fg='red',command=root.destroy,font=('Calibri'))
btn5.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="About", bg='black', fg='green',command=about,font=('Calibri'))
btn5.place(relx=0.05, rely=0.9, relwidth=0.1, relheight=0.05)

root.mainloop()