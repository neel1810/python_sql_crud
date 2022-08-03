from pymysql import *
from tkinter import *

win = Tk()
win.title("Student Management")
win['bg']='yellow'
win.geometry("100009x10009+0+0")

name_info=StringVar()
sid_info=IntVar()
course_info=StringVar()

def save():
    a = open(r"C:\Users\Aryan\Desktop\student_management.txt",mode='a')
    b = open(r"C:\Users\Aryan\Desktop\student_management.csv",mode='a')
    name=name_info.get()
    sid=sid_info.get()
    course=course_info.get()
    print("Student name: ",name)
    print("Student Id: ",sid)
    print("Student educational course: ",course)
    if name=="":
        messagebox.showerror("Error","Name cannot be empty")
    elif sid>50 or sid<=0:
        messagebox.showerror("Error","Student Id cannot be greater than 50 or less than/equal to 0")
    else:
        Label(win,text="Student added successfully",font="arial 15 bold",bg='yellow').place(x=200,y=350)
    b.write("{},{},{}".format(name,sid,course))
    a.write("\nName: {} ".format(name))
    a.write("\nStudent Id: {} ".format(sid))
    a.write("\nStudent educational course: {} ".format(course))
    a.close()
    b.close()

def savedb():
    name=name_info.get()
    sid=sid_info.get()
    course=course_info.get()
    print("Student name: ",name)
    print("Student Id: ",sid)
    print("Student educational course: ",course)
    if name=="":
        messagebox.showerror("Error","Name cannot be empty")
    elif sid>50 or sid<=0:
        messagebox.showerror("Error","Student Id cannot be greater than 50 or less than/equal to 0")
    else:
        Label(win,text="Student added successfully",font="arial 15 bold",bg='yellow').place(x=200,y=350)
    conn = connect(host='localhost',user='root',password='aryan07',database='students_management')
    cur = conn.cursor()
    cur.execute('insert into students value("{}",{},"{}");'.format(name,sid,course))
    conn.commit()
    conn.close()

def shdb():
    conn = connect(host='localhost',user='root',password='aryan07',database='students_management')
    cur = conn.cursor()
    cur.execute('select * from students;')
    v=0
    for i in cur:
        Label(win,text=i,font="arial 12 bold",bg='yellow').place(x=200,y=250+v)
        v+=30
    conn.commit()
    conn.close()

def deldb():
    conn = connect(host='localhost',user='root',password='aryan07',database='students_management')
    cur = conn.cursor()
    cur.execute('delete from students where sid={}'.format(sid_info.get()))
    Label(win,text='Student Deleted Successfully',
          font="arial 12 bold",
          bg='yellow').place(x=200,y=350)
    conn.commit()
    conn.close()


##Label
name = Label(win,text="Enter your name: ",font="arial 15 bold",bg='yellow').place(x=20,y=30)
s_id = Label(win,text="Enter your student Id: ",font="arial 15 bold",bg='yellow').place(x=20,y=80)
course = Label(win,text="Enter your educational course: ",font="arial 15 bold",bg='yellow').place(x=20,y=130)

##Entry
name = Entry(win,text=" ",font="arial 15 bold",textvariable=name_info).place(x=350,y=30)
sid = Entry(win,text=" ",font="arial 15 bold",textvariable=sid_info).place(x=350,y=80)
course = Entry(win,text=" ",font="arial 15 bold",textvariable=course_info).place(x=350,y=130)

##Button
Button(win,text="Save",font='15',bg='yellow',command=savedb).place(x=100,y=200)
Button(win,text="Show",font='15',bg='yellow',command=shdb).place(x=300,y=200)
Button(win,text="Delete",font='15',bg='yellow',command=deldb).place(x=400,y=200)

win.mainloop()



