"""
Program to creat a database of books with
various functions.
"""
from tkinter import *
import back

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    b1.delete(0,END)
    b1.insert(END,selected_tuple[1])
    b2.delete(0,END)
    b2.insert(END,selected_tuple[2])
    b3.delete(0,END)
    b3.insert(END,selected_tuple[3])
    b4.delete(0,END)
    b4.insert(END,selected_tuple[4])


def view_command():
    list1.delete(0,END)
    for row in back.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in back.search(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()):
        list1.insert(END,row)

def add_command():
    back.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()))

def delete_command():
    back.delete(selected_tuple[0])

def update_command():
    back.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())


window=Tk()

window.wm_title("Book Store")

a1=Label(window,text="Title")
a1.grid(row=0,column=0)

a2=Label(window,text="Author")
a2.grid(row=0,column=2)

a3=Label(window,text="Year")
a3.grid(row=2,column=0)

a4=Label(window,text="ISBN")
a4.grid(row=2,column=2)

title_text=StringVar()
b1=Entry(window,textvariable=title_text)
b1.grid(row=0,column=1)

author_text=StringVar()
b2=Entry(window,textvariable=author_text)
b2.grid(row=0,column=3)

year_text=StringVar()
b3=Entry(window,textvariable=year_text)
b3.grid(row=2,column=1)

ISBN_text=StringVar()
b4=Entry(window,textvariable=ISBN_text)
b4.grid(row=2,column=3)

list1=Listbox(window,height=13,width=50)
list1.grid(row=3,column=0,rowspan=5,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

c1=Button(window,text="View All", width=14,command=view_command)
c1.grid(row=3,column=3)

c2=Button(window,text="Search Entry", width=14,command=search_command)
c2.grid(row=4,column=3)

c3=Button(window,text="Add Entry", width=14,command=add_command)
c3.grid(row=5,column=3)

c4=Button(window,text="Update", width=14,command=update_command)
c4.grid(row=6,column=3)

c5=Button(window,text="Delete", width=14,command=delete_command)
c5.grid(row=7,column=3)

c6=Button(window,text="Close", width=14,command=window.destroy)
c6.grid(row=8,column=3)


window.mainloop()
