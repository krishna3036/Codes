# This is a sample Report Program. It fetches data from my user_details table to display
from tkinter import ttk
import tkinter as tk
import sqlite3
import datetime as dt
database = "U:\A-Spring-2023\Combined-BIS698\PythonCodes\Database\database_698.db"
#conn = sqlite3.connect(database)

def connect():

    conn = sqlite3.connect(database)

    cur = conn.cursor()


def View():

    my_tag = 'normal'
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_details")

    rows = cur.fetchall()
    for row in rows:
        if my_tag == 'normal':
            my_tag = 'gray'
        else:
            my_tag = 'normal'
        #print(row)

        tree.insert("", tk.END, values=row, tags=my_tag)

    conn.close()

def Exit():  # Exits the program
    root.destroy()



# connect to the database

connect()

root = tk.Tk()
root.option_add('*Font', '18', )
#root.option_add('Calibri', '20')
root.title()

frame = tk.Frame(root)
frame.pack()

#root.geometry('1000x600')

user_info_frame = tk.LabelFrame(frame, text="", background='')
user_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

report_label = tk.Label(user_info_frame, text="Report on the Users in the System", font='Calibri, 15', anchor="c")
report_label.grid(row=0, column=0)
date = dt.datetime.now()


date_label = tk.Label(user_info_frame, text=f"{date:%A, %B %d, %Y}", font="Calibri, 12", anchor='e')
date_label.grid(row=1, column=0)  # r=1, column = 0


report_frame = tk.LabelFrame(frame, text="", background='')
report_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

#Add a Vertical Scrollbar



s = ttk.Style()
s.theme_use('clam')
font1 = ['Times', 12, 'normal']
# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', background="lightgray", font=font1)

# Add a Treeview widget
#tree= ttk.Treeview(win, column=("c1", "c2"), show='headings', height=8)



tree = ttk.Treeview(report_frame,column=("1", "2", "3", "4", "5", "6"), show='headings')


tree.tag_configure('gray', background='lightgray')
tree.tag_configure('normal', background='white')

tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="UserID", )
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Firstname")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Middlename")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Lastname")
tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="Country")
tree.column("#6", anchor=tk.CENTER)
tree.heading("#6", text="Gender")

#tree.grid(row=3, column=0)
tree.pack()

button_frame = tk.LabelFrame(frame, text="", background='')
button_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

btnDisplay = tk.Button(button_frame, text="Display", width=10, command=View)
btnExit = tk.Button(button_frame, text="Exit", width=10, command=Exit)

btnDisplay.grid(row=0, column=0, pady=10)
btnExit.grid(row=0, column=1,pady=10)

for widget in button_frame.winfo_children():
    widget.grid_configure(padx=30, pady=10)

root.mainloop()

