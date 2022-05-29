#=========Importing Libraries=========#

import tkinter as tk
from tkinter import *
import sys
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import Image,ImageTk


#=========All the define statements=========#

def command1(event):
    if entry1.get() == 'Admin' and entry2.get() == "Admin":
        root.deiconify()
        top.destroy()
    elif entry1.get() == '' and entry2.get() == "":
        MessageBox.showerror("Empty Credentials","Username/Password cannot be empty.")
    else:
        MessageBox.showerror('Invalid Credentials', 'Please recheck your Username/Password.')


def command2():
    top.destroy()
    root.destroy()
    sys.exit()

def printi():
    id = e_Eid.get()
    name = e_FN.get()
    name2 = e_LN.get()
    phone = e_PH.get()
    condi = cond

    if id == "" or phone == "":
        MessageBox.showinfo('Insert Status', 'All fields are required')
    else:
        con = mysql.connect(host='localhost', user="root", password="2312", database="emergency_portal")
        cursor = con.cursor()
        cursor.execute("insert into patientdata values('" + id + "','" + name + "','" + name2 + "','" + phone + "','" + condi +"'," + "CURRENT_TIMESTAMP()" + ")")
        cursor.execute("commit")

        e_Eid.delete(0, 'end')
        e_FN.delete(0, 'end')
        e_LN.delete(0, 'end')
        e_PH.delete(0, 'end')
        show()
        MessageBox.showinfo('Insert Status', "Inserted Successfully")
        con.close()

def printu():
    id = e_Eid.get()
    name = e_FN.get()
    name2 = e_LN.get()
    phone = e_PH.get()

    if id == "" or phone == "":
        MessageBox.showinfo('Update Status', "All fields are required")
    else:
        con = mysql.connect(host='localhost', user="root", password="2312", database="emergency_portal")
        cursor = con.cursor()
        cursor.execute("update patientdata set e_FN='" + name + "',e_PH='" + phone + "',e_LN='" + name2 + "' where e_Eid='" + id + "'")
        cursor.execute("commit")

        e_Eid.delete(0, 'end')
        e_FN.delete(0, 'end')
        e_LN.delete(0, 'end')
        e_PH.delete(0, 'end')
        show()
        MessageBox.showinfo('Update Status', "Updated Successfully")
        con.close()

def printd():
    if (e_Eid.get() == ''):
        MessageBox.showinfo("Delete Status", "Emirates ID is compulsary")
    else:
        con = mysql.connect(host='localhost', user="root", password="2312", database="emergency_portal")
        cursor = con.cursor()
        cursor.execute("delete from patientdata where e_Eid='" + e_Eid.get() + "'")
        cursor.execute("commit")

        e_Eid.delete(0, 'end')
        e_FN.delete(0, 'end')
        e_LN.delete(0, 'end')
        e_PH.delete(0, 'end')
        show()
        MessageBox.showinfo('Delete Status', "Deleted Successfully")
        con.close()

def gett():
    if (e_Eid.get() == ""):
        MessageBox.showinfo("Fetch Status", "Emirates ID Number is compulsory")
    else:
        con = mysql.connect(host='localhost', user='root', password='2312', database='emergency_portal')
        cursor = con.cursor()
        cursor.execute("select * from patientdata where e_Eid='" + e_Eid.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e_FN.insert(0, row[1])
            e_PH.insert(0, row[3])
            e_LN.insert(0, row[2])

        con.close()

def show():
    con = mysql.connect(host='localhost', user='root', password='2312', database='emergency_portal')
    cursor = con.cursor()
    cursor.execute("select * from patientdata")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = str(row[0]) + "    " + row[3]  + "    " + row[1]  + "    " + row[2]
        list.insert(list.size() + 1, insertData)
    con.close()

def radbutton():
    global x
    global cond
    x = Val.get()

    if x == 0:
        cond = "Critical"
    elif x == 1:
        cond = "Severe"
    elif x == 2:
        cond = "Moderate"
    elif x == 3:
        cond = "Mild"

def create_window():
    import matplotlib.pyplot as plt
    import mysql.connector
    import numpy as np
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='2312',
        database='emergency_portal')
    cur = mydb.cursor()
    s = "select count(e_FN) from patientdata group by cond"
    cur.execute(s)
    result = cur.fetchall()

    cur1 = mydb.cursor()
    p = "select cond from patientdata group by cond"
    cur1.execute(p)
    result1 = cur1.fetchall()

    values = []
    namesh = []

    for rec in result:
        values.append(rec)
    for n in result1:
        namesh.append(n)

    VALUES2 = np.array(namesh)
    values2 = np.array(values)

    noofpeeps = values2.flatten()
    CondofP = VALUES2.flatten()

    plt.pie(noofpeeps, labels=CondofP, wedgeprops={"edgecolor":"black"},autopct="%0.2f%%", shadow='True')
    plt.show()

def screen():
    nx = Tk()
    nx.geometry("500x650")
    nx.maxsize(500,650)
    nx.minsize(500,650)
    nx.title("Patient Data")
    label = Label(nx, text="Detailed Patient Data", font = "time 20 bold" , bg="#685698", fg="white", padx = 115 , pady = 20)
    label.grid(row = 0, column=0, columnspan=20)


    p1 = Label(nx, text = "Date & Time",font="time 10 bold")
    p1.grid(row = 1 , column = 1 , padx = 10 , pady = 10)

    p2 = Label(nx, text = "Id", font="time 10 bold")
    p2.grid(row=1, column = 2, padx=10, pady=10)

    p3 = Label(nx, text = "First name", font="time 10 bold")
    p3.grid(row=1, column = 3, padx=10, pady=10)

    p4 = Label(nx, text = "Last name", font="time 10 bold")
    p4.grid(row=1, column = 4, padx=10, pady=10)

    con = mysql.connect(host='localhost', user="root", password="2312", database="emergency_portal")
    cursor = con.cursor()
    cursor.execute("select * from patientdata")

    r = cursor.fetchall()

    num = 2
    for i in r:
        Date = Label(nx, text = i[5], font = "time 9 bold", fg = "black" )
        Date.grid(row = num, column = 1 , padx = 10,pady = 10 )

        ID = Label(nx, text=i[0], font="time 9 bold", fg="black")
        ID.grid(row=num, column=2, padx=10, pady=10)

        FNAME = Label(nx, text=i[1], font="time 9 bold", fg="black")
        FNAME.grid(row=num, column=3, padx=10, pady=10)

        LNAME = Label(nx, text=i[2], font="time 9 bold", fg="black")
        LNAME.grid(row=num, column=4, padx=10, pady=10)

        num= num+1

    con.commit()
    con.close()


#=========Code for creating the login window=========#

root = Tk()
top = Toplevel()

top.geometry('500x250')
top.maxsize(500,250)
top.minsize(500,250)
top.title("User Login")
top.iconbitmap(r"Med_Icon.ico")

#=========Canvas layout picture=========#

canvas = tk.Canvas(top,height=400,width=600)
imgpath='BackPic.jpg'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

image = canvas.create_image(0,0,image=photo)
canvas.place(x=0,y=0)

Label(top, text="Emergency Portal",bg="#184E72",font="Haettenschweiler 32", fg= "Black").pack(side = TOP)
lbl1 = Label(top, text="Username:", font=("Helevtica", 13), fg = "white")
lbl1.configure(background="#184E72")                           #7C72DC    #32373E
entry1 = Entry(top)

lbl2 = Label(top, text="Password:", font=("Helevtica", 13) , fg = "white")
lbl2.configure(background="#184E72") #7C72DC
entry2 = Entry(top, show="*")

button2 = Button(top, text="Cancel",command=lambda: command2())
entry2.bind("<Return>", command1)

lbl3 = Label(top, text="Made with Python and Tkinter \n © to 'Respective Hospital'", font=("Ariel", 9))
lbl3.configure(background="#184E72")

lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()

lbl3.pack(side=BOTTOM)
button2.pack(side = BOTTOM)


#=========The Main Window Codes Starts from here=========#

root.geometry("700x350")
root.maxsize(700,350)
root.minsize(700,350)
root.title("EMERGENCY PORTAL")
root.iconbitmap(r"Med_Icon.ico")
load = Image.open("C:\\Users\\shath\\Documents\\Transfered\\School Stuffs\\Informatics\Project\\BackPic.jpg")
render = ImageTk.PhotoImage(load)
iimg = Label(root,image = render)
iimg.place(x=0,y=0)

#=========Code used to add the Program Title=========#

Label(root, text='Emergency Portal', font=('Coolvetica Rg', 25),fg="white",bg="#021325").pack(side=TOP, padx=10)

#=========Codes used for labelling the Entry Boxes=========#

FN = Label(root, text="First Name:", font=("bold", 10),fg="white",bg="#021125")
FN.place(x=20, y=40)

LN = Label(root, text="Last Name:", font=("bold", 10),fg="white",bg="#021125")
LN.place(x=150, y=40)

Eid = Label(root, text="Emirates ID Number:", font=("bold", 10),fg="white",bg="#021125")
Eid.place(x=20, y=100)

PH = Label(root, text="Phone No.", font=("bold", 10),fg="white",bg="#041122")
PH.place(x=20, y=160)

#=========Code to get entries from the User=========#

e_FN = Entry()
e_FN.place(x=20, y=60)

e_LN = Entry()
e_LN.place(x=150, y=60)

e_Eid = Entry()
e_Eid.place(x=20, y=120)

e_PH = Entry()
e_PH.place(x=20, y=180)

#=====These Codes are used for creating the Buttons=====#

insert = Button(root, text="Add Patient", font=("italic", 10), bg="lightgreen", command=printi)
insert.place(x=20, y=240)

update = Button(root, text="Update", font=("italic", 10), bg="lightyellow", command=printu)
update.place(x=110, y=240)

delete = Button(root, text="Delete", font=("italic", 10), bg="pink", command=printd)
delete.place(x=175, y=240)

get = Button(root, text="Get", font=("italic", 10), bg="lightblue", command=gett)
get.place(x=230, y=240)

NWB = Button(root, text="Charts", font=("italic", 10), bg="lightgreen", command=create_window)
NWB.place(x=300, y=270)

get = Button(root, text="Show", font=("italic", 10), bg="lightblue", command=screen)
get.place(x=375, y=270)

#===================Scroll Bars===================#

Fr=Frame(root)
Fr.place(x=300, y=70)
sbr = Scrollbar(Fr)
sbr2 = Scrollbar(Fr,orient='horizontal')
sbr2.pack(side=BOTTOM, fill ="x")
sbr.pack(side=RIGHT,fill="y")

list = Listbox(Fr,width=45,height=10)
list.pack()
show()

sbr.config(command=list.yview)
sbr2.config(command=list.xview)
list.config(yscrollcommand=sbr.set)
list.config(xscrollcommand=sbr2.set)


#==========Patients Condition==========#

Val = IntVar()


CB_Critical = Radiobutton(root, text="Critical",fg="#E11800",bg="#021125", variable = Val, value = 0, command=radbutton)
CB_Critical.place(x=180, y=100)
CB_Critical.invoke()

CB_Severe = Radiobutton(root, text="Severe",fg="#FF8F00",bg="#021125", variable = Val, value = 1, command=radbutton)
CB_Severe.place(x=180, y=120)

CB_Moderate = Radiobutton(root, text="Moderate",fg="#ECF825",bg="#021125", variable = Val, value = 2, command=radbutton)
CB_Moderate.place(x=180, y=140)

CB_Mild = Radiobutton(root, text="Mild",fg="#7DFF00",bg="#021125", variable = Val, value = 3, command=radbutton)
CB_Mild.place(x=180, y=160)


root.withdraw()
root.mainloop()