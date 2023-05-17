#Comments are Filipino(Tagalog) Based. Feel free to Google Translate. 
#Made by Mark Dennis Concha and Jay-r Donesa.
#Under The Supervision of Mr. Manuel Sentillas
#REMOVE ALL BITMAP OR REPLACE THE ICO FILE TO AVOID RUNTIME ERRORS!!!!

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

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Berlin Sans FB', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("STEM PTECH IMMERSION PROJECT")
root.config(bg=('#48426D'))
root.iconbitmap(r'Icon.ico')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


window_width = 1050
window_height = 700


x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set ng Window geometry
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


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
        root.iconbitmap(r'Icon.ico')
           
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
            root.iconbitmap(r'Icon.ico')
            return

    refreshTable()
    
def clear():
    # Check if any entry is empty
    if not studidEntry.get() or not studnameEntry.get() or not ageEntry.get() or not departmentEntry.get() or not professorEntry.get():
        # Display an error message box
        messagebox.showerror("Error", "There is nothing to Clear 🤔 ")
    else:
        # Clear all entries
        studidEntry.delete(0, 'end')
        studnameEntry.delete(0, 'end')
        ageEntry.delete(0, 'end')
        departmentEntry.delete(0, 'end')
        professorEntry.delete(0, 'end')
 
  
# Delete Button na Function
def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    root.iconbitmap(r'Icon.ico')
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
            root.iconbitmap(r'Icon.ico')
            return

        refreshTable()
# Pag Declare at Style ng mg Values
label = Label(root, text="STUDENT CRUD", font=('Berlin Sans FB', 28),bg=('#48426D'),fg=('#F0C38E'))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

studidLabel = Label(root, text="Student ID:", font=('Berlin Sans FB Bold', 15),bg=('#48426D'),fg=('#F0C38E'))
studnameLabel = Label(root, text="Sudent Name:", font=('Berlin Sans FB Bold', 15),bg=('#48426D'),fg=('#F0C38E'))
ageLabel = Label(root, text="Student Age:", font=('Berlin Sans FB Bold', 15),bg=('#48426D'),fg=('#F0C38E'))
departmentLabel = Label(root, text="Student Department:", font=('Berlin Sans FB Bold', 15),bg=('#48426D'),fg=('#F0C38E'))
professorLabel = Label(root, text="Student Professor:", font=('Berlin Sans FB Bold', 15),bg=('#48426D'),fg=('#F0C38E'))

studidLabel.grid(row=3, column=0, columnspan=1, padx=75, pady=5)
studnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
ageLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
departmentLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
professorLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

studidEntry = Entry(root, width=45, bd=3, font=('Berlin Sans FB', 15),bg=('#312C51'),fg=('#F0C38E'), textvariable = ph1)
studnameEntry = Entry(root, width=45, bd=3, font=('Berlin Sans FB', 15),bg=('#312C51'),fg=('#F0C38E'), textvariable = ph2)
ageEntry = Entry(root, width=45, bd=3, font=('Berlin Sans FB', 15),bg=('#312C51'),fg=('#F0C38E'), textvariable = ph3)
departmentEntry = Entry(root, width=45, bd=3, font=('Berlin Sans FB', 15),bg=('#312C51'),fg=('#F0C38E'), textvariable = ph4)
professorEntry = Entry(root, width=45, bd=3, font=('Berlin Sans FB', 15),bg=('#312C51'),fg=('#F0C38E'), textvariable = ph5)

studidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
studnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
ageEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
departmentEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
professorEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=1, 
    bd=10, font=('Berlin Sans FB', 15),bg=('#F0C38E'),fg=('#48426D'), command=add)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=1,
    bd=10, font=('Berlin Sans FB', 15),bg=('#F0C38E'),fg=('#48426D'), command=delete)
clearBtn = Button(
    root, text="Clear", padx=65, pady=25, width=1, 
    bd=10, font=('Berlin Sans FB', 15),bg=('#F0C38E'),fg=('#48426D'), command=clear)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
clearBtn.grid(row=7, column=5, columnspan=1, rowspan=2)

#ttk.Style Para sa Color ng Tree
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", font=('Berlin Sans FB Bold', 15),background='#F0C38E',foreground='#48426D')
style.map('Treeview',background=[('selected','sandy brown')])
my_tree['columns'] = ("StudentID","StudentName","Age","Department","Professor")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("StudentID", anchor=W, width=170)
my_tree.column("StudentName", anchor=W, width=170)
my_tree.column("Age", anchor=W, width=170)
my_tree.column("Department", anchor=W, width=170)
my_tree.column("Professor", anchor=W, width=170)

my_tree.heading("StudentID", text="Student ID", anchor=W)
my_tree.heading("StudentName", text="Student Name", anchor=W)
my_tree.heading("Age", text="Age", anchor=W)
my_tree.heading("Department", text="Department", anchor=W)
my_tree.heading("Professor", text="Professor", anchor=W)

refreshTable()

#Mainloop Ending
root.mainloop()
