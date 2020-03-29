from tkinter import *
from backend import Database
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk

database = Database()

def get_selected_row(event):
    try:
        global selected_row
        index = list1.curselection()[0]
        selected_row = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_row[1])
        e2.delete(0,END)
        e2.insert(END, selected_row[2])
        e3.delete(0,END)
        e3.insert(END, selected_row[3])
        e4.delete(0,END)
        e4.insert(END, selected_row[4])
        e5.delete(0,END)
        e5.insert(END, selected_row[5])
        e6.delete(0,END)
        e6.insert(END, selected_row[6])
        e7.delete(0,END)
        e7.insert(END, selected_row[7])
        e8.delete(0,END)
        e8.insert(END, selected_row[8])
        e9.delete(0,END)
        e9.insert(END, selected_row[9])
    except IndexError :
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(name_text.get(), itype_text.get(), amount_text.get(), sdate_text.get(), ldate_text.get(), anav_text.get(), qty_text.get(), holder_text.get(), portal_text.get()):
        list1.insert(END,row)

def insert_command():
    list1.delete(0,END)
    database.insert(name_text.get(), itype_text.get(), amount_text.get(), sdate_text.get(), ldate_text.get(), anav_text.get(), qty_text.get(), holder_text.get(), portal_text.get())
    list1.insert(END, name_text.get(), itype_text.get(), amount_text.get(), sdate_text.get(), ldate_text.get(), anav_text.get(), qty_text.get(), holder_text.get(), portal_text.get())

def delete_command():
    database.delete(selected_row[0])
    emptycells()

def update_command():
    database.update(selected_row[0],name_text.get(), itype_text.get(), amount_text.get(), sdate_text.get(), ldate_text.get(), anav_text.get(), qty_text.get(), holder_text.get(), portal_text.get())
    emptycells()

def emptycells():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    view_command()


window = Tk()
window.wm_title("Investment Manager")
window.configure(bg="#242024")
window.iconbitmap(default='icon.ico')

name_text = StringVar()
l1 = tk.Label(window, text = "Scheme/Shares Name", font = "Times 15 bold", bg = '#242024', fg="white")
l1.grid(row = 0, column = 0, pady = 5, padx = 5)
e1 = Entry(window, textvariable = name_text, width = 80, font = "Courier 14")
e1.grid(row = 0, column = 1, columnspan = 4, pady = 5, padx = 5)
e1.focus_force() 

itype_text = StringVar()
l2 = tk.Label(window, text = "Investment Type", font = "Times 15 bold", bg = '#242024', fg="white")
l2.grid(row = 1, column = 0, pady = 5, padx = 5)
e2 = Entry(window, textvariable = itype_text, font = "Courier 14")
e2.grid(row = 1, column = 1, pady = 5, padx = 5)

amount_text = StringVar()
l3 = tk.Label(window, text = "Total Amount", font = "Times 15 bold", bg = '#242024', fg="white")
l3.grid(row = 1, column = 3, pady = 5, padx = 5)
e3 = Entry(window, textvariable = amount_text, font = "Courier 14")
e3.grid(row = 1, column = 4, pady = 5, padx = 5)

sdate_text = StringVar()
l4 = tk.Label(window, text = "Start Date", font = "Times 15 bold", bg = '#242024', fg="white")
l4.grid(row = 2, column = 0, pady = 5, padx = 5)
e4 = Entry(window, textvariable = sdate_text, font = "Courier 14")
e4.grid(row = 2, column = 1, pady = 5, padx = 5)

ldate_text = StringVar()
l5 = tk.Label(window, text = "Last Inv Date", font = "Times 15 bold", bg = '#242024', fg="white")
l5.grid(row = 2, column = 3, pady = 5, padx = 5)
e5 = Entry(window, textvariable = ldate_text, font = "Courier 14")
e5.grid(row = 2, column = 4, pady = 5, padx = 5)

anav_text = StringVar()
l6 = tk.Label(window, text = "Average NAV/Price", font = "Times 15 bold", bg = '#242024', fg="white")
l6.grid(row = 3, column = 0, pady = 5, padx = 5)
e6 = Entry(window, textvariable = anav_text, font = "Courier 14")
e6.grid(row = 3, column = 1, pady = 5, padx = 5)

qty_text = StringVar()
l7 = tk.Label(window, text = "Quantity", font = "Times 15 bold", bg = '#242024', fg="white")
l7.grid(row = 3, column = 3, pady = 5, padx = 5)
e7 = Entry(window, textvariable = qty_text, font = "Courier 14")
e7.grid(row = 3, column = 4, pady = 5, padx = 5)

holder_text = StringVar()
l8 = tk.Label(window, text = "Holder's Name", font = "Times 15 bold", bg = '#242024', fg="white")
l8.grid(row = 4, column = 0, pady = 5, padx = 5)
e8 = Entry(window, textvariable = holder_text, font = "Courier 14")
e8.grid(row = 4, column = 1, pady = 5, padx = 5)

portal_text = StringVar()
l9 = tk.Label(window, text = "Portal", font = "Times 15 bold", bg = '#242024', fg="white")
l9.grid(row = 4, column = 3, pady = 5, padx = 5)
e9 = Entry(window, textvariable = portal_text, font = "Courier 14")
e9.grid(row = 4, column = 4, pady = 5, padx = 5)


# This will create style object 
style = Style() 
  
# This will be adding style, and  
# naming that style variable as  
# W.Tbutton (TButton is used for ttk.Button). 
  
style.configure('ViewSearch.TButton', font = ('calibri', 10, 'bold'), background = '#5bc0de', borderwidth = '5', relief=SUNKEN )
style.configure('Delete.TButton', font = ('calibri', 10, 'bold'), background = '#d9534f')
style.configure('Close.TButton', font = ('calibri', 10, 'bold'), borderwidth = '5', background = '#f0ad4e')
style.configure('AddUpdate.TButton', font = ('calibri', 10, 'bold'), background = '#5cb85c')

view_button = tk.Button(window, text = "View All", width = 20, bg = '#5bc0de', fg = 'white', font = "Times 14 bold", borderwidth = '3', command = view_command)
view_button.grid(row = 5, column=0, pady = 5, padx = 5)

search_button = tk.Button(window, text = "Search", width = 20, bg = '#5bc0de', fg = 'white', font = "Times 14 bold",borderwidth = '3', command = search_command)
search_button.grid(row = 5, column=2, pady = 5, padx = 5)

delete_button = tk.Button(window, text = "Delete", width = 20, bg = '#d9534f', fg = 'white', font = "Times 14 bold",borderwidth = '3', command = delete_command)
delete_button.grid(row = 5, column=4, pady = 5, padx = 5)

add_button = tk.Button(window, text = "Add", width = 20, bg = '#5cb85c', fg = 'white', font = "Times 14 bold",borderwidth = '3', command = insert_command)
add_button.grid(row = 6, column=0, pady = 5, padx = 5)

update_button = tk.Button(window, text = "Update", width = 20, bg = '#428bca', fg = 'white', font = "Times 14 bold",borderwidth = '3', command = update_command)
update_button.grid(row = 6, column=2, pady = 5, padx = 5)

close_button = tk.Button(window, text = "Close", width = 20, bg = '#f0ad4e', fg = 'white', font = "Times 14 bold", borderwidth = '3', command = window.destroy)
close_button.grid(row = 6, column=4, pady = 5, padx = 5)

list1 = Listbox(window, height = 6, width = 120, bg ="#9a9a9a", bd ='5', fg = "white", font = "Times 14", selectbackground = '#a29bfe')
list1.grid(row= 7, column = 0, rowspan = 4, columnspan = 5, pady = 5, padx = 5)
"""bg = "grey", 
                  activestyle = 'dotbox',  
                  font = "Helvetica", 
                  fg = "yellow"
                  """

sb1 = tk.Scrollbar(window)
sb1.grid(row = 7, column = 5, rowspan = 4)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop()