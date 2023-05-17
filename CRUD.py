#Comments are Filipino(Tagalog) Based. Feel free to Google Translate. 
#Made by Mark Dennis Concha and Jay-r Donesa.
#Under The Supervision of Mr. Manuel Sentillas

import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
 


#Ito yung Connection Para sa pyMYSQL
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='stud_db',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Work Immersion CRUD")
root.geometry("1080x720")

my_tree = ttk.Treeview(root)

#Place Holder Para sa Mga Entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#Value Function ng mga Placeholder
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

# Add Button na Function
def add():
    studid = str(studidEntry.get())
    studname = str(studnameEntry.get())
    age = str(ageEntry.get())
    department = str(departmentEntry.get())
    professor = str(professorEntry.get())

    if (studid == "" or studid == " ") or (studname == "" or studname == " ") or (age == "" or age == " ") or (department == "" or department == " ") or (professor == "" or professor == " "):
        messagebox.showinfo("Error","Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students VALUES ('"+studid+"','"+studname+"','"+age+"','"+department+"','"+professor+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()
    
# Reset Button na Function
def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()
# Delete Button na Function
def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE STUDID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()
#Select Button na Function
def select():
    try:
        selected_item = my_tree.selection()[0]
        studid = str(my_tree.item(selected_item)['values'][0])
        studname = str(my_tree.item(selected_item)['values'][1])
        age = str(my_tree.item(selected_item)['values'][2])
        department = str(my_tree.item(selected_item)['values'][3])
        professor = str(my_tree.item(selected_item)['values'][4])

        setph(studid,1)
        setph(studname,2)
        setph(age,3)
        setph(department,4)
        setph(professor,5)
    except:
        messagebox.showinfo("Error", "Please select a data row")

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE STUDID='"+
    studid+"' or studname='"+
    studname+"' or age='"+
    age+"' or department='"+
    department+"' or professor='"+
    professor+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

# Update Button na Function
def update():
    selectedStudid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedStudid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    studid = str(studidEntry.get())
    studname = str(studnameEntry.get())
    age = str(ageEntry.get())
    department = str(departmentEntry.get())
    professor = str(professorEntry.get())

    if (studid == "" or studid == " ") or (studname == "" or studname == " ") or (age == "" or age == " ") or (department == "" or department == " ") or (professor == "" or professor == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET STUDID='"+
            studid+"', studname='"+
            studname+"', age='"+
            age+"', department='"+
            department+"', professor='"+
            professor+"' WHERE STUDID='"+
            selectedStudid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()

# Pag Declare at Style ng mg Values
label = Label(root, text="STEM PTECH 12B STUDENT CRUD", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

studidLabel = Label(root, text="Student ID", font=('Arial', 15))
studnameLabel = Label(root, text="Sudent Name", font=('Arial', 15))
ageLabel = Label(root, text="Age", font=('Arial', 15))
departmentLabel = Label(root, text="Department", font=('Arial', 15))
professorLabel = Label(root, text="Professor", font=('Arial', 15))

studidLabel.grid(row=3, column=0, columnspan=1, padx=75, pady=5)
studnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
ageLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
departmentLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
professorLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

studidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
studnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
ageEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
departmentEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
professorEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

studidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
studnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
ageEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
departmentEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
professorEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=1, 
    bd=5, font=('Arial', 15), bg="#ed9898", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=1,
    bd=5, font=('Arial', 15), bg="#ed9898", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=1,
    bd=5, font=('Arial', 15), bg="#ed9898", command=delete)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=1,
    bd=5, font=('Arial', 15), bg="#ed9898", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=1,
    bd=5, font=('Arial', 15), bg="#ed9898", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=11, column=5, columnspan=1, rowspan=2)

#ttk.Style Para sa Color ng Tree
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", font=('Arial Bold', 15))
style.map('Treeview',background=[('selected','pink')])
my_tree['columns'] = ("StudentID","StudentName","Age","Department","Professor")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("StudentID", anchor=W, width=170)
my_tree.column("StudentName", anchor=W, width=150)
my_tree.column("Age", anchor=W, width=150)
my_tree.column("Department", anchor=W, width=165)
my_tree.column("Professor", anchor=W, width=150)

my_tree.heading("StudentID", text="Student ID", anchor=W)
my_tree.heading("StudentName", text="Student Name", anchor=W)
my_tree.heading("Age", text="Age", anchor=W)
my_tree.heading("Department", text="Department", anchor=W)
my_tree.heading("Professor", text="Professor", anchor=W)

refreshTable()

#Mainloop Ending
root.mainloop()
