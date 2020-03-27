from tkinter import *
import backend

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
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(name_text.get(), itype_text.get(), amount_text.get(), sdate_text.get(), ldate_text.get(), anav_text.get(), qty_text.get(), holder_text.get(), portal_text.get()):
        list1.insert(END,row)

def insert_command():
    list1.delete(0,END)
    backend.insert(name_text.get(), itype_text.get(), amount_text.get(), sdate_text.get(), ldate_text.get(), anav_text.get(), qty_text.get(), holder_text.get(), portal_text.get())
    list1.insert(END, name_text.get(), itype_text.get(), amount_text.get(), sdate_text.get(), ldate_text.get(), anav_text.get(), qty_text.get(), holder_text.get(), portal_text.get())

def delete_command():
    backend.delete(selected_row[0])
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

def update_command():
    backend.update(selected_row[0],name_text.get(), itype_text.get(), amount_text.get(), sdate_text.get(), ldate_text.get(), anav_text.get(), qty_text.get(), holder_text.get(), portal_text.get())
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

name_text = StringVar()
l1 = Label(window, text = "Scheme/Fund Name")
l1.grid(row = 0, column = 0)
e1 = Entry(window, textvariable = name_text, width = 70)
e1.grid(row = 0, column = 1, columnspan = 4)

itype_text = StringVar()
l2 = Label(window, text = "Investment Type")
l2.grid(row = 1, column = 0)
e2 = Entry(window, textvariable = itype_text)
e2.grid(row = 1, column = 1)

amount_text = StringVar()
l3 = Label(window, text = "Total Amount")
l3.grid(row = 1, column = 3)
e3 = Entry(window, textvariable = amount_text)
e3.grid(row = 1, column = 4)

sdate_text = StringVar()
l4 = Label(window, text = "Start Date")
l4.grid(row = 2, column = 0)
e4 = Entry(window, textvariable = sdate_text)
e4.grid(row = 2, column = 1)

ldate_text = StringVar()
l5 = Label(window, text = "Last Inv Date")
l5.grid(row = 2, column = 3)
e5 = Entry(window, textvariable = ldate_text)
e5.grid(row = 2, column = 4)

anav_text = StringVar()
l6 = Label(window, text = "Average NAV")
l6.grid(row = 3, column = 0)
e6 = Entry(window, textvariable = anav_text)
e6.grid(row = 3, column = 1)

qty_text = StringVar()
l7 = Label(window, text = "Quantity")
l7.grid(row = 3, column = 3)
e7 = Entry(window, textvariable = qty_text)
e7.grid(row = 3, column = 4)

holder_text = StringVar()
l8 = Label(window, text = "Holder's Name")
l8.grid(row = 4, column = 0)
e8 = Entry(window, textvariable = holder_text)
e8.grid(row = 4, column = 1)

portal_text = StringVar()
l9 = Label(window, text = "Portal")
l9.grid(row = 4, column = 3)
e9 = Entry(window, textvariable = portal_text)
e9.grid(row = 4, column = 4)

view_button = Button(window, text = "View All", width = 20, command = view_command)
view_button.grid(row = 5, column=0)

update_button = Button(window, text = "Update", width = 20, command = update_command)
update_button.grid(row = 5, column=2)

delete_button = Button(window, text = "Delete", width = 20, command = delete_command)
delete_button.grid(row = 5, column=4)

add_button = Button(window, text = "Add", width = 20, command = insert_command)
add_button.grid(row = 6, column=0)

search_button = Button(window, text = "Search", width = 20, command = search_command)
search_button.grid(row = 6, column=2)

close_button = Button(window, text = "Close", width = 20, command = window.destroy)
close_button.grid(row = 6, column=4)

list1 = Listbox(window, height = 6, width = 100)
list1.grid(row= 7, column = 0, rowspan = 4, columnspan = 5)

sb1 = Scrollbar(window)
sb1.grid(row = 7, column = 5, rowspan = 4)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop()