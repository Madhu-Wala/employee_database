from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from sqlite3 import *
from requests import *
import json
import pandas as pd
import matplotlib.pyplot as plt
import requests
import sqlite3

mw=Tk()
mw.title("APP")
mw.geometry("1350x620+50+50")
mw.configure(bg="cornsilk")
f=("Cambria",16,"bold")

#FUNCTIONS ---------------------

def f1():
    mw.withdraw()
    aw.deiconify()

def f2():
    mw.deiconify()
    aw.withdraw()
    aw_ent1.delete(0,END)
    aw_ent2.delete(0,END)
    aw_ent3.delete(0,END)
    aw_ent1.focus()

def f3():
    mw.withdraw()
    vw.deiconify()
    vw_emp_data.delete(1.0,END)
    con=None
    try:
        con=connect("ems.db")
        cursor=con.cursor()
        sql="select * from employee"
        cursor.execute(sql)
        data=cursor.fetchall()
        info=" "
        for d in data:
            info=info+"Employee id: "+str(d[0])+"  Employee name: "+str(d[1])+"  Salary: "+str(d[2])+"\n"
        vw_emp_data.insert(INSERT,info)
    except Exception as e:
        showerror("Issue" ,e)
    finally:
        if con is not None:
            con.close()

def f4():
    vw.withdraw()       
    mw.deiconify()

def f5():
    mw.withdraw()
    uw.deiconify()

def f6():
    uw.withdraw()
    mw.deiconify()

def f7():
    mw.withdraw()
    dw.deiconify()

def f8():
    dw.withdraw()
    mw.deiconify()

def f9():
    con=None
    try:
        con=connect("ems.db")
        cursor=con.cursor()
        sql="insert into employee values('%d','%s','%f')"
        try:
            id=int(aw_ent1.get())
        except ValueError:
            showerror("Issue","Enter integres only")
            aw_ent1.delete(0,END)
            aw_ent1.focus()
            return
        if id<1 :
            showerror("Issue","Enter valid id")
            aw_ent1.delete(0,END)
            aw_ent1.focus()
            return
        cursor.execute("SELECT id FROM employee WHERE id=?",(id,))
        existing_id=cursor.fetchone()
        if existing_id:
            showerror("Issue","Id already exists")
            aw_ent1.delete(0,END)
            aw_ent1.focus()
            return
        name=aw_ent2.get()
        try:
            if not name.isalpha():
                showerror("Issue","Name must contain alphabets only")
                aw_ent2.delete(0,END)
                aw_ent2.focus()
                return
            if len(name)<2:
                showerror("Issue","Name must contain minimum 2 characters")
                aw_ent2.delete(0,END)
                aw_ent2.focus()
                return
        except Exception as e:
            showerror("Issue",e)
        try:
             salary=float(aw_ent3.get())
        except ValueError():
            showerror("Issue","Please enter salary")
            aw_ent3.delete(0,END)
            aw_ent3.focus()
            return
        if salary<8000:
            showerror("Issue","Salary should be minimum ₹8000")
            aw_ent3.delete(0,END)
            aw_ent3.focus()
            return
        cursor.execute(sql%(id,name,salary))
        con.commit()
        showinfo("Record added") 
        aw_ent1.delete(0,END)
        aw_ent2.delete(0,END)
        aw_ent3.delete(0,END)
        aw_ent1.focus()
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()

def f10():
    con=None
    try:
        con=connect("ems.db")
        cursor=con.cursor()
        sql="update employee set name='%s',salary='%f' where id='%d'"
        try:
            id=int(uw_ent1.get())
        except ValueError:
            showerror("Isssue","Id must contain integer value only")
            uw_ent1.delete(0,END)
            uw_ent1.focus()
            return
        if id<1:
            showerror("Issue","Enter valid id")
            uw_ent1.delete(0,END)
            uw_ent1.focus()
            return
        name=uw_ent2.get()
        if not name.isalpha():
            showerror("Issue","Name must contain alphabets only")
            uw_ent2.delete(0,END)
            uw_ent2.focus()
            return
            
        if len(name)<2:
            showerror("Issue","Name must contain minimum two alphabets")
            uw_ent2.delete(0,END)
            uw_ent2.focus()
            return
        try:
            salary=float(uw_ent3.get())
        except ValueError:
            showerror("Issue","Salary must contain numerical values only")
            uw_ent3.delete(0,END)
            uw_ent3.focus()
            return  
        if salary<8000:
            showerror("Issue","Salary should be minimum ₹8000")
            uw_ent3.delete(0,END)
            uw_ent3.focus()
            return      
        cursor.execute(sql%(name,salary,id))
        if cursor.rowcount==1:
            showinfo("Record updated")
            uw_ent1.delete(0,END)
            uw_ent2.delete(0,END)
            uw_ent3.delete(0,END)
            uw_ent1.focus()
        else:
            showerror("Issue","Record does not exist")
            uw_ent1.delete(0,END)
            uw_ent2.delete(0,END)
            uw_ent3.delete(0,END)
            uw_ent1.focus()
        con.commit()
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()

def f11():
    con=None
    try:
        con=connect('ems.db')
        cursor=con.cursor()
        sql="delete from employee where id='%d'"
        try:
            id=int(dw_ent1.get())
        except ValueError:
            showerror("Issue","Id must contain integers only")
            dw_ent1.delete(0,END)
            dw_ent1.focus()
            return
        if id<1:
            showerror("Issue","Enter valid id")
            dw_ent1.delete(0,END)
            dw_ent1.focus()
            return
        cursor.execute(sql%(id))
        if cursor.rowcount==1:
            con.commit()
            showinfo("Record Deleted")  
        else:
            showerror("Record does not exist")
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()
        dw_ent1.delete(0,END)
        dw_ent1.focus()

def f12():
    try:
        send_url="http://ip-api.com/json/"
        geo_req=requests.get(send_url)
        geo_json=json.loads(geo_req.text)
        city=geo_json['city']
        lab.configure(text=city)
    except Exception as e:
        showerror("Issue",e)
    try:
                a1="https://api.openweathermap.org/data/2.5/weather"
                a2="?q="+city
                a3="&appid="+ "c6e315d09197cec231495138183954bd"
                a4="&units="+"metric"
                wa=a1+a2+a3+a4
                print(wa)
                res=get(wa)
                data=res.json()
                temp= data['main']['temp']
                tem.configure(text=temp)
    except Exception as e:
                showerror("Issue",e)

def f13():
    conn=sqlite3.connect('ems.db')
    df=pd.read_sql_query("SELECT name,salary FROM employee ORDER BY salary DESC LIMIT 5",conn)
    plt.bar(df['name'],df['salary'])
    plt.xlabel('Name')
    plt.ylabel('Salary')
    plt.title("Top 5 salaries")
    plt.show()
    conn.close()


#MAIN window----------------

mw_add=Button(mw,text="Add data",font=f,width=10,command=f1)
mw_add.place(x=80,y=80)
mw_view=Button(mw,text="View data",font=f,width=10,command=f3)
mw_view.place(x=340,y=80)
mw_update=Button(mw,text="Update data",font=f,width=10,command=f5)
mw_update.place(x=600,y=80)
mw_delete=Button(mw,text="Delete data",font=f,width=10,command=f7)
mw_delete.place(x=860,y=80)
mw_charts=Button(mw,text="Graph",font=f,width=10,command=f13)
mw_charts.place(x=1120,y=80)
mw_lab_location=Label(mw,text="Location: ",font=f,bg="cornsilk")
mw_lab_location.place(x=200,y=330)
mw_lab_temp=Label(mw,text="Temprature: ",font=f,bg="cornsilk")
mw_lab_temp.place(x=200,y=380)
lab=Label(mw,font=f,wraplength=700,bg="cornsilk")
lab.place(x=480,y=330)
tem=Label(mw,font=f,wraplength=700,bg="cornsilk")
tem.place(x=480,y=380)
f12()


#ADD window-------------------

aw=Toplevel(mw)
aw.title("Add data")
aw.configure(bg="lightcyan")
aw.geometry("1200x620+50+50")
aw_lab1=Label(aw,text="Enter id: ",font=f,bg="lightcyan")
aw_ent1=Entry(aw,font=f,width=10)
aw_lab2=Label(aw,text="Enter name: ",font=f,bg="lightcyan")
aw_ent2=Entry(aw,font=f,width=10)
aw_lab3=Label(aw,text="Enter salary: ",font=f,bg="lightcyan")
aw_ent3=Entry(aw,font=f,width=10)
aw_lab1.pack(pady=10)
aw_ent1.pack(pady=10)
aw_lab2.pack(pady=10)
aw_ent2.pack(pady=10)
aw_lab3.pack(pady=10)
aw_ent3.pack(pady=10)
aw_save=Button(aw,text="Save",font=f,width=10,command=f9,bg="dodgerblue",fg="white")
aw_back=Button(aw,text="Back",font=f,width=10,command=f2,bg="powderblue")
aw_save.pack(pady=10)
aw_back.pack(pady=10)
aw.withdraw()

#VIEW window -------------------

vw=Toplevel(mw)
vw.title("View")
vw.geometry("1200x670+50+50")
vw_emp_data=ScrolledText(vw,width=65,height=10,font=f)
vw_emp_data.pack(pady=10)
vw_back=Button(vw,text="Back",font=f,width=10,command=f4,bg="powderblue")
vw_back.pack(pady=10)
vw.withdraw()

#UPDATE window-------------

uw=Toplevel(mw)
uw.title("Update")
uw.configure(bg="lightcyan")
uw.geometry("1200x620+50+50")
uw_lab1=Label(uw,text="Enter id: ",font=f,bg="lightcyan")
uw_lab1.pack(pady=10)
uw_ent1=Entry(uw,font=f,width=10)
uw_ent1.pack(pady=10)
uw_lab2=Label(uw,text="Enter name: ",font=f,bg="lightcyan")
uw_lab2.pack(pady=10)
uw_ent2=Entry(uw,font=f,width=10)
uw_ent2.pack(pady=10)
uw_lab3=Label(uw,text="Enter salary: ",font=f,bg="lightcyan")
uw_lab3.pack(pady=10)
uw_ent3=Entry(uw,font=f,width=10)
uw_ent3.pack(pady=10)
uw_save=Button(uw,text="Save",font=f,width=10,command=f10,bg="dodgerblue",fg="white")
uw_save.pack(pady=10)
uw_back=Button(uw,text="Back",font=f,width=10,command=f6,bg="powderblue")
uw_back.pack(pady=10)
uw.withdraw()

#DELETE window

dw=Toplevel(mw)
dw.title("Delete")
dw.geometry("1200x620+50+50") 
dw.configure(bg="papayawhip")
dw_lab1=Label(dw,text="Enter id of employee whose record is to be deleted: ",font=f,bg="papayawhip")
dw_lab1.pack(pady=10)
dw_ent1=Entry(dw,font=f,width=10)
dw_ent1.pack(pady=10)
dw_del=Button(dw,text="Delete",font=f,width=10,command=f11,bg="palevioletred",fg="white")
dw_del.pack(pady=10)
dw_back=Button(dw,text="Back",font=f,width=10,command=f8,bg="powderblue")
dw_back.pack(pady=10)
dw.withdraw()

mw.mainloop()
