from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sqlite3

#-------------------------------------------functions---------------------------------------------------------------------------------------#
def iexit():
    ex=messagebox.askyesno("Student database management system","Confirm if you want to exit")
    if ex>0:
        scr.destroy()
    return
def opens():
    global cu
    global li
    global con
    n=filedialog.askopenfilename()
    con=sqlite3.connect(n)
    cu=con.cursor()
    cu.execute('''SELECT 
    name
FROM 
    sqlite_master 
WHERE 
    type ='table' AND 
    name NOT LIKE "sqlite_%"''')
    li.delete(0,END)
    n=0
    for i in list(cu):
        li.insert(n,i)
        n+=1
def getdata():
    global cu
    global li
    global li1
    
    li1.delete(0,END)
    try:
        table=li.get(li.curselection())
        cu.execute('select * from {}'.format(*table))
        n=0
        for i in list(cu):
           
            li1.insert(n,i)
            n+=1
    except:
        pass
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

def new():
     
    root=Tk(className='NEW FILE')
    v3=StringVar()
    e3=Entry(root,textvariable=v3,font=('times',15,'bold'),bg='cadet blue',width=20)
    e3.place(x=70,y=50)
    lf=Label(root,text='enter the location where you want the file to be saved',bg='yellow',font=('times',12,'bold'))
    lf.place(x=80,y=10)
    def ok():
        a=sqlite3.connect(e3.get())
        cu=a.cursor()
        cu.execute('create table student(firstname varchar(7), lastname varchar(14), age int, gender varchar(6),id int unique)')
    b7=Button(root,text='0K',command=ok)
    b7.grid(row=1,column=0)

    
def display():
    a=li1.get(li1.curselection())
    v1.set(a[0])
    v2.set(a[1])
    v3.set(a[2])
    v4.set(a[3])
    v5.set(a[4])
    
def update():
    global cu
    global con
    cu.execute("insert into student values(%r,%r,%d,%r,%d)"%(e1.get(),e2.get(),int(e3.get()),e4.get(),int(e5.get())))
    con.commit()
def delete():
    global cu
    global con
    cu.execute("delete from student where id=?",(e5.get()))
    con.commit()
    
def edit():
    global cu
    global con
    cu.execute("update student  set firstname=? where id=? ",(e1.get(),e5.get()))
    cu.execute("update student  set lastname=? where id=? ",(e2.get(),e5.get()))
    cu.execute("update student  set age=? where id=? ",(e3.get(),e5.get()))
    cu.execute("update student  set gender=? where id=? ",(e4.get(),e5.get()))
    con.commit()



def search():
    global li1
    global cu
    global con
   
    def match(a):
        li1.delete(0,END)
        j=0
        for i in a:
            li1.insert(j,i)
            j=j+1
        
    if(e1.get()!='' and e2.get()=='' and e3.get()=='' and e4.get()=='' and e5.get()==''   ):
        cu.execute('select * from student where firstname=?',(e1.get(),))
        n=cu.fetchall()
        match(n)
    if(e2.get()!='' and e1.get()=='' and e3.get()=='' and e4.get()=='' and e5.get()==''):
        cu.execute('select * from student where lastname=?',(e2.get(),))
        n1=cu.fetchall()
        match(n1)
    if(e3.get()!='' and e2.get()=='' and e1.get()=='' and e4.get()=='' and e5.get()==''):
        cu.execute('select * from student where age=?',(e3.get(),))
        n2=cu.fetchall()
        match(n2)
    if(e4.get()!='' and e2.get()=='' and e3.get()=='' and e1.get()=='' and e5.get()==''):
        cu.execute('select * from student where gender=?',(e4.get(),))
        n3=cu.fetchall()
        match(n3)
    if(e5.get()!='' and e2.get()=='' and e3.get()=='' and e4.get()=='' and e1.get()==''):
        cu.execute('select * from student where id=?',(e5.get(),))
        n5=cu.fetchall()
        match(n5)
    
    if(e1.get()!='' and e2.get()!='' ):
        cu.execute('select * from student where firstname=? and lastname=?',(e1.get(),e2.get()))
        n6=cu.fetchall()
        match(n6)
    if(e1.get()!='' and e3.get()!='' ):
        cu.execute('select * from student where firstname=? and age=?',(e1.get(),e3.get()))
        n7=cu.fetchall()
        match(n7)
    if(e1.get()!='' and e4.get()!='' ):
        cu.execute('select * from student where firstname=? and gender=?',(e1.get(),e4.get()))
        n8=cu.fetchall()
        match(n8)
    if(e1.get()!='' and e5.get()!='' ):
        cu.execute('select * from student where firstname=? and id=?',(e1.get(),e5.get()))
        n9=cu.fetchall()
        match(n9)
    if(e2.get()!='' and e3.get()!='' ):
        cu.execute('select * from student where lastname=? and age=?',(e2.get(),e3.get()))
        n10=cu.fetchall()
        match(n10)
    if(e2.get()!='' and e4.get()!='' ):
        cu.execute('select * from student where lastname=? and gender=?',(e2.get(),e4.get()))
        n11=cu.fetchall()
        match(n11)
    if(e2.get()!='' and e5.get()!='' ):
        cu.execute('select * from student where lastname=? and id=?',(e2.get(),e5.get()))
        n12=cu.fetchall()
        match(n12)
    if(e3.get()!='' and e4.get()!='' ):
        cu.execute('select * from student where age=? and gender=?',(e3.get(),e4.get()))
        n13=cu.fetchall()
        match(n13)
    if(e3.get()!='' and e5.get()!=''):
        cu.execute('select * from student where age=? and id=?',(e3.get(),e5.get()))
        n14=cu.fetchall()
        match(n14)
    if(e4.get()!='' and e5.get()!=''):
        cu.execute('select * from student where gender=? and id=?',(e4.get(),e5.get()))
        n15=cu.fetchall()
        match(n15)
    
        
         
       
   
   
    
       
    
    
   

    
               


#----------------------------------------------------------buttons and listboxes-----------------------------------------#
scr=Tk(className=" STUDENT DATABASE MANGEMENT SYSTEM")
scr.geometry('1200x800+0+0')
b=Button(scr,text='open',command=opens)
b.grid(row=0,column=0)
b1=Button(scr,text='create',command=new)
b1.grid(row=0,column=1)
b2=Button(scr,text='delete',command=delete)
b2.grid(row=0,column=2)
b3=Button(scr,text='update',command=update)
b3.grid(row=0,column=3)
b4=Button(scr,text='clear',command=clear)
b4.grid(row=0,column=4)
b5=Button(scr,text='exit',command=iexit)
b5.grid(row=0,column=5)
b6=Button(scr,text='display',command=display)
b6.grid(row=0,column=6)
b7=Button(scr,text='edit',command=edit)
b7.grid(row=0,column=7)
b8=Button(scr,text='Search',command=search)
b8.grid(row=0,column=8)
f=Frame(scr,bg='white')
f.grid(row=1,columnspan=10)
li=Listbox(f,font=('times',20,'bold'))
li.grid(row=0,column=0)
b4=Button(f,text='get data',command=getdata)
b4.grid(row=1,column=0)
f1=Frame(scr,bg='blue')
f1.grid(row=2,columnspan=5)

x=Label(scr,text='First Name',font=('times',12,'bold'),bg='white')
x.place(x=0,y=400)
v1=StringVar()
e1=Entry(scr,textvariable=v1,font=('times',15,'bold'),bg='cadet blue',width=10)
e1.place(x=80,y=400)
v1.trace('w',lambda *args:v1.set((v1.get())[:10]))



y=Label(scr,text='Last Name',font=('times',12,'bold'),bg='white')
y.place(x=0,y=440)
v2=StringVar()
e2=Entry(scr,textvariable=v2,font=('times',15,'bold'),bg='cadet blue',width=10)
e2.place(x=80,y=440)
v2.trace('w',lambda *args:v1.set((v1.get())[:10]))


z=Label(scr,text='Age',font=('times',12,'bold'),bg='white')
z.place(x=0,y=480)
v3=StringVar()
e3=Entry(scr,textvariable=v3,font=('times',15,'bold'),bg='cadet blue',width=10)
e3.place(x=80,y=480)
v3.trace('w',lambda *args:v3.set((v3.get())[:2]))


x1=Label(scr,text='Gender',font=('times',12,'bold'),bg='white')
x1.place(x=0,y=520)
v4=StringVar()
e4=Entry(scr,textvariable=v4,font=('times',15,'bold'),bg='cadet blue',width=10)
e4.place(x=80,y=520)
v4.trace('w',lambda *args:v4.set((v4.get())[:6]))

x2=Label(scr,text='StudentId',font=('times',12,'bold'),bg='white')
x2.place(x=0,y=560)
v5=StringVar()
e5=Entry(scr,textvariable=v5,font=('times',15,'bold'),bg='cadet blue',width=10)
e5.place(x=80,y=560)
v5.trace('w',lambda *args:v5.set((v5.get())[:10]))



li1=Listbox(f,font=('times',20,'bold'),bg='red',width=40)
li1.grid(row=0,column=3)







