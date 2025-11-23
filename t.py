from d import Inputdata
from tkinter import *
from tkinter import messagebox
new1=Inputdata("f:/adiban-contacts/eleman.db")
# ==========================win main==========================
win = Tk()
x = win.winfo_screenwidth()
y = win.winfo_screenheight()
x1 = 450
y1 = 650
xwin = (x // 2) - (x1 // 2)
ywin = (y // 2) - (y1 // 2)
win.geometry(f'{x1}x{y1}+{xwin}+{ywin}')
win.title("contacts")
win.config(bg='#8E6B14')


# ==========================general==========================
def adout():
    messagebox.showinfo('About', 'program name: contacts-manage \nWritten by: Ahmad Adiban \n    Data : 03/04/2024')


def exit():
    ask1 = messagebox.askyesno('Exit', 'Are you sure:')
    if ask1 == 1:
        win.destroy()


# -----------------------------------------------------------------------------------------
b_about = Button(win, text='About', font=('Wide Latin', 5), fg="white", bg='black', width=6, height=3, command=adout)
b_exit = Button(win, text='Exit', font=('Wide Latin', 5), fg="white", bg='black', width=6, height=3, command=exit)

b_about.place(x=1, y=615)
b_exit.place(x=389, y=615)


# ------------------------------------fun-----------------------------------------------------
def insert():
    en1 = not_use(fname_entry.get())
    en2 = not_use(lname_entry.get())
    en3 = not_use(address_entry.get())
    en4 = not_use(tel_entry.get())

    if en1 and en2 and en3 and en4 != "" and en4.isdigit():
        new1.insert(en1.capitalize(),en2.capitalize(),en3.capitalize(),en4)
        
        clear()
        show_list()
    else:
        messagebox.showerror('Error', 'please fill in fields')


def delete():
    global item
    result = messagebox.askyesno('delete', 'are you sure?')
    if result:
        new1.remove(item[0])
        show_list()
        clear()

    

def clear():
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    address_entry.delete(0, END)
    tel_entry.delete(0, END)
    fname_entry.focus_set()


def deleteall():
    result = messagebox.askyesno('delete', 'are you sure?')
    if result:
        list1.delete(0 , END)

def select_item(event):
    global item
    index=list1.curselection()
    item=list1.get(index)
    clear()
    fname_entry.insert(0,item[1])
    lname_entry.insert(0,item[2])
    address_entry.insert(0,item[3])
    tel_entry.insert(0,item[4])
    update_but.config(state=NORMAL)
    delete_but.config(state=NORMAL)

def update():
     global item
     en1 = not_use(fname_entry.get())
     en2 = not_use(lname_entry.get())
     en3 = not_use(address_entry.get())
     en4 = not_use(tel_entry.get())
     if en1 and en2 and en3 and en4 != "" and en4.isdigit():
        new1.update(item[0],en1.capitalize(),en2.capitalize(),en3.capitalize(),en4)
        clear()
        show_list()
     else:
        messagebox.showerror('Error', 'please fill in fields')
     
     


def show_list():
    list1.delete(0,END)
    for fild in new1.select():
        list1.insert(END , fild)

def search():
    mase_lab.config(text='')
    cheng1=search_entry.get().capitalize().replace('*','%')
    cheng2=cheng1.replace('?','_')
    search_text=new1.search(var.get(),cheng2)
    search_entry.delete(0,END)
    list1.delete(0,END)
    if not search_text:
        mase_lab.config(text='not found this item')
        search_entry.focus()
    else:
        list1.delete(0,END)
        for fild in search_text:
            list1.insert(END , fild)

def not_use(word:str)->str:  # not use '*' or '?'
    num1=word.count('*')
    num2=word.count('?')
    if num1==0 and num2==0:
        return word
    else:
            messagebox.showerror('error', 'Dont use of the character * or ?')
            clear()
        

# ------------------------------------weget-----------------------------------------------------
fname_lab = Label(win, text='fname:', bg='#8E6B14', font=('titr', 10))
lname_lab = Label(win, text='lname:', bg='#8E6B14', font=('titr', 10))
address_lab = Label(win, text='Address:', bg='#8E6B14', font=('titr', 10))
tel_lab = Label(win, text='Tel:', bg='#8E6B14', font=('titr', 10))
mase_lab=Label(win, text='',  fg= 'red' , bg='#8E6B14', font=('titr', 20))
search_lab = Label(win, text='search item:',  fg= '#06067C' , bg='#8E6B14', font=('titr', 10))
fname_entry = Entry(win, bd=5, bg='#F4E6C2')
lname_entry = Entry(win, bd=5, bg='#F4E6C2')
address_entry = Entry(win, bd=5, bg='#F4E6C2')
tel_entry = Entry(win, bd=5, bg='#F4E6C2')
search_entry = Entry(win, bd=5, bg='#F4E6C2')
search_but = Button(win, text='search', font=('aria', 10), fg='white', bg='black', width=8, height=2, bd=3,
                    command=search)
insert_but = Button(win, text='insert', font=('aria', 10), fg='white', bg='black', width=8, height=2, bd=3,
                    command=insert)
delete_but = Button(win,state=DISABLED, text='delete', font=('aria', 10), fg='white', bg='black', width=8, height=2, bd=3,
                    command=delete)
show_list_but = Button(win, text='showlist', font=('aria', 10), fg='white', bg='black', width=8, height=2, bd=3,
                       command=show_list)
clear_but = Button(win, text='clear', font=('aria', 10), fg='white', bg='black', width=8, height=2, bd=3, command=clear)
deleteall_but = Button(win, text='delete list', font=('aria', 10), fg='white', bg='black', width=8, height=2, bd=3,
                    command=deleteall)
update_but = Button(win,state=DISABLED, text='update', font=('aria', 10), fg='white', bg='black', width=8, height=2, bd=3,
                    command=update)
list1 = Listbox(win, width=30, height=13, bg='#D0CCEA', font=('roya', 12))
scor=Scrollbar(win)
d1={'fname':'fname' , 'lname':'lname' , 'address':'address' , 'phone':'phone'}
var=StringVar()
var.set('fname')
step=1
for i,j in d1.items():
    choese_search=Radiobutton(win , text=i , value=j , variable=var ,  font = ('titr' , 8) , bg='#8E6B14')
    choese_search.place(x=92*step , y=450)
    step+=1


#----------------------------------------------place--------------------------------------------------
fname_entry.focus_set()
fname_lab.place(x=8, y=10)
lname_lab.place(x=230, y=10)
address_lab.place(x=8, y=50)
tel_lab.place(x=230, y=50)
mase_lab.place(x=100 , y= 550)
search_lab.place(x=0 , y=450)
fname_entry.place(x=80, y=10)
lname_entry.place(x=280, y=10)
address_entry.place(x=80, y=50)
tel_entry.place(x=280, y=50)
search_entry.place(x=180, y=510)
search_but.place(x=60, y=500)
insert_but.place(x=80, y=100)
delete_but.place(x=350, y=240)
show_list_but.place(x=350, y=170)
clear_but.place(x=280, y=100)
deleteall_but.place(x=350, y=310)
update_but.place(x=350, y=380)
list1.place(x=35, y=170)
scor.place(x=310 , y=170 , height=250)
scor.config(command = list1.yview)
list1.bind('<<ListboxSelect>>',select_item)
#radin forked this project to work on it and this is a random change
win.mainloop()
