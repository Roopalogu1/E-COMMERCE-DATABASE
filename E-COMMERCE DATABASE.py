import pymysql
from tkinter import*
from tkinter import messagebox
from tabulate import tabulate

def create_database():
    cnx=pymysql.connect(host="localhost",user="root",password="roopa")
    cursor=cnx.cursor()
    query="create database amazon"
    cursor.execute(query)
    cursor.close()
    cnx.close()
    

def create_table():
    cnx=pymysql.connect(host="localhost",user="root",password="roopa",database="amazon")
    cursor=cnx.cursor()
    query="create table products(sno int primary key,pname varchar(200),qty int,price int)"
    cursor.execute(query)

    query1="insert into products(sno,pname,qty,price)values(%s,%s,%s,%s)"
    record=[(1,"pencil",10,2),(2,"pen",10,5),(3,"books",10,100),(4,"file",10,20),(5,"bag",10,100)]
    cursor.executemany(query1,record)

    cnx.commit()
    cursor.close()
    cnx.close()
    

def insert():
    sno=e1.get()
    pname=e2.get()
    qty=e3.get()
    price=e4.get()
    cnx=pymysql.connect(host="localhost",user="root",password="roopa",database="amazon")
    cursor=cnx.cursor()
    query="insert into products(sno,pname,qty,price)values(%s,%s,%s,%s)"
    record=(sno,pname,qty,price)
    cursor.execute(query,record)
    messagebox.showinfo("INSERTING","the data are inserted")
    print("data inserted successfully")
    cnx.commit()
    cursor.close()
   
    cnx.close()
def update():
    sno=e1.get()
    pname=e2.get()
    qty=e3.get()
    price=e4.get()
    cnx=pymysql.connect(host="localhost",user="root",password="roopa",database="amazon")
    cursor=cnx.cursor()
    query="update products set pname=%s,qty=%s,price=%s where sno=%s"
   
    record=(pname,qty,price,sno)
    cursor.execute(query,record)
    messagebox.showinfo("UPDATION","the database is updated")
    print("the database is updated with the new data")
    cnx.commit()
    cursor.close()
    
    cnx.close()
def select():
   cnx=pymysql.connect(host="localhost",user="root",password="roopa",database="amazon")
   cursor=cnx.cursor()
   query="select * from products"
   cursor.execute(query)
   rows=cursor.fetchall()
   print(tabulate(rows,headers=["S.No","PNAME","QUANTITY","PRICE"]))
   cursor.close()
   cnx.close()
def delete():
   sno=e1.get()
   cnx=pymysql.connect(host="localhost",user="root",password="roopa",database="amazon")
   cursor=cnx.cursor()
   query="delete from products where sno=%s"
   users=(sno)
   cursor.execute(query,users)
   messagebox.showinfo("DELETE","the DATA deleted from the database")
   print("the data is deleted from the database")
   cnx.commit()
   cursor.close()
   cnx.close()

def drop():
    cnx=pymysql.connect(host="localhost",user="root",password="roopa",database="amazon")
    cursor=cnx.cursor()
    query="drop database amazon"
    cursor.execute(query)
    messagebox.showinfo("exiting","the database is dropped")
    print("the  database is dropped")
    cnx.commit()
    cursor.close()
    
    cnx.close()

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def main():
    create_database()
    create_table()

    root = Tk()
    root.title("AMAZON - 'YOUR EVERYDAY SHOPPING!!!'")
    root.geometry("600x500")
    root.configure(bg="pink")
    global e1
    global e2
    global e3
    global e4
    global sno
    global pname
    global qty
    global price

    
    #the required widgets are added and grid() is used as geometry maanger
    label=Label(root,text="ENTER THE DETAILS",font=("times",20,"bold"),fg="purple",bg="pink")
    label.grid(row=0,column=1)

    label1 = Label(root, text="S.No:", font=("times", 16),bg="pink")
    e1=Entry(root)
   
    label1.grid(row=5, column=0)
    e1.grid(row=5,column=1)

    label2 = Label(root, text="PRODUCT NAME:", font=("times", 16),bg="pink")
    e2=Entry(root)
    
    label2.grid(row=7, column=0)
    e2.grid(row=7,column=1)

    label3 = Label(root, text="QUANTITY:", font=("times", 16),bg="pink")
    e3=Entry(root)
    
    label3.grid(row=9, column=0)
    e3.grid(row=9,column=1)

    label4 = Label(root, text="PRICE:", font=("times", 16),bg="pink")
    e4=Entry(root)
  
    label4.grid(row=11, column=0)
    e4.grid(row=11,column=1)

    button1=Button(root,text="VIEW TABLE",font=("calibri",16),command=select,fg="purple",width=10,height=1)
    button1.grid(row=5,column=3)

    button2=Button(root,text="INSERT",font=("calibri",16),command=insert,fg="purple",width=10,height=1)
    button2.grid(row=7,column=3)

    button3=Button(root,text="UPDATE",font=("calibri",16),command=update,fg="purple",width=10,height=1)
    button3.grid(row=9,column=3)

    button4=Button(root,text="DELETE",font=("calibri",16),command=delete,fg="purple",width=10,height=1)
    button4.grid(row=11,column=3)

    button5=Button(root,text="EXIT",font=("calibri",16),bg="purple",command=drop,fg="white",width=10,height=1)
    button5.grid(row=27,column=1)

    button6=Button(root,text="CLEAR ENTRY",font=("calibri",16),bg="purple",command=clear,fg="white",width=10,height=1)
    button6.grid(row=20,column=1)

    root.mainloop()

if __name__ == "__main__":
    main()


