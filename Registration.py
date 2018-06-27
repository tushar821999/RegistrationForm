from tkinter import *
# setup container configuration
from PIL import ImageTk,Image
import sqlite3
conn = sqlite3.connect("registration.db")
cursor = conn.cursor()

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

img = ImageTk.PhotoImage(Image.open('boy.png'))
panel = Label(root,image=img)
panel.place(x=220,y=23)

lable_0 = Label(root,text="Registration Form",width = 20,font=("bold",15),fg='black')
lable_0.place(x=140,y=83)

lable_1 = Label(root,text="Full Name",width = 20,font=("bold",10),fg='black')
lable_1.place(x=80,y=130)
names = StringVar()
entry_1 = Entry(root,textvariable=names)
entry_1.place(x=240,y=130)

lable_2 = Label(root,text="E-mail",width = 20,font=("bold",10),fg='black')
lable_2.place(x=68,y=180)

emails = StringVar()
entry_2 = Entry(root,textvariable=emails)
entry_2.place(x=240,y=180)

lable_3 = Label(root,text="Gender",width = 20,font=("bold",10),fg='black')
lable_3.place(x=70,y=230)

var = StringVar()
Radiobutton(root,text="Male",padx=5,variable=var,value='male').place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=var,value='female').place(x=290,y=230)
'''
#for option menu
lable_4 = Label(root,text="country",width=20,font=("bold",10),fg='black')
lable_4.place(x=70,y=280)


list1 = ['Canada','India','UK','Nepal','Iceland','South  Africa']
c=StringVar()
droplist = OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set("Select your country")
droplist.place(x=240,y=280)
'''
lable_4 = Label(root,text="Password",width=20,font=("bold",10),fg='black')
lable_4.place(x=70,y=280)
passwords = StringVar()
entry_3 = Entry(root,show='*',textvariable=passwords)
entry_3.place(x=235,y=280)
'''
#for checkbutton
lable_5 = Label(root,text="Programming",width=20,font=("bold",10),fg='black')
lable_5.place(x=85,y=330)
var1 = StringVar()
cb1 = Checkbutton(root,text="java",variable=var1).place(x=235,y=330)
var2 = StringVar()
cb2 = Checkbutton(root,text="python",variable=var2).place(x=290,y=330)
'''
lable_5 = Label(root,text="Pin Code",width=20,font=("bold",10),fg='black')
lable_5.place(x=70,y=330)
pincodes = StringVar()
entry_4 = Entry(root,textvariable=pincodes)
entry_4.place(x=235,y=330)


lable_6 = Label(root,text="Not Saved",width=20,font=("bold",10),fg='red')
lable_6.place(x=170,y=420)

def clicked():
    if(conn):
        print("Database Opened And Created Successfully")
    else:
        print("Database Not Found")

    name = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    pincode = entry_4.get()
    gender = var.get()

    ct = conn.execute("CREATE TABLE IF NOT EXISTS Details(name varchar2(40),email varchar2(40),password varchar2(40),pincode varchar2(40),gender varchar2(40));")
    if(ct):
        print("Create Details Table Succesfully")
    else:
        print("Creation Table Error Occured")

    cursor.execute("insert into Details(name,email,password,pincode,gender) values (?,?,?,?,?)",(name,email,password,pincode,gender))

    conn.commit()

    data = name+" "+email+" "+password+" "+pincode+" "+gender

    lable_6.configure(text="Data Saved",fg='green')

Button(root,text="Submit",width=20,bg='brown',fg='white',command=clicked).place(x=90,y=380)

def show():
    data = conn.execute("select * from Details")
    for row in data:
        print("name : ",row[0]," email : ",row[1]," password : ",row[2]," pincode : ",row[3]," gender : ",row[4])
    lable_6.configure(text="Data Showed",fg='orange')
    conn.close()
Button(root,text="Show",width=20,bg='brown',fg='white',command=show).place(x=280,y=380)


mainloop()