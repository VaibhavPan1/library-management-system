from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import pymysql

mypass = "" #enter the database password
mydatabase="db" #enter the database name here

con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
# Enter Table Names here
issueTable = "books_issued"
bookTable = "books" #Book Table


def deleteBook():
    bid = bookInfo1.get()

    deleteSql = "delete from " + bookTable + " where bid = '" + bid + "'"
    deleteIssue = "delete from " + issueTable + " where bid = '" + bid + "'"

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()

        messagebox.showinfo('Success', "Book Record Deleted Successfully")

    except:
        messagebox.showinfo("Please check Book ID")

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()


def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Delete Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="grey")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Delete Button
    SubmitBtn = ttk.Button(root, text="DELETE", command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = ttk.Button(root, text="Quit", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
