from tkinter import END, Button, Entry, Tk
##Gui Interaction
window = Tk()
window.geometry("500x500")
## Adding Inputs
e = Entry(window, width=30, bg="white", borderwidth=5)
e.place(x=100, y=0)


def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))


button = Button(window, text="1", width=5, command=lambda: click(1))
button.place(x=10, y=30)
button = Button(window, text="2", width=5, command=lambda: click(2))
button.place(x=80, y=30)
button = Button(window, text="3", width=5, command=lambda: click(3))
button.place(x=150, y=30)
button = Button(window, text="4", width=5, command=lambda: click(4))
button.place(x=220, y=30)
button = Button(window, text="5", width=5, command=lambda: click(5))
button.place(x=290, y=30)
button = Button(window, text="6", width=5, command=lambda: click(6))
button.place(x=360, y=30)
button = Button(window, text="7", width=5, command=lambda: click(7))
button.place(x=10, y=60)
button = Button(window, text="8", width=5, command=lambda: click(8))
button.place(x=80, y=60)
button = Button(window, text="9", width=5, command=lambda: click(9))
button.place(x=150, y=60)
button = Button(window, text="0", width=5, command=lambda: click(0))
button.place(x=220, y=60)


#Operators
def dot():
    e.delete(0, END)


button = Button(window, text=".", width=5, command=dot)
button.place(x=290, y=60)


def AC():
    e.delete(0, END)


button = Button(window, text="AC", width=5, command=AC)
button.place(x=10, y=90)


def Cancel():
    e.delete(0, END)


button = Button(window, text="C", width=5, command=Cancel)
button.place(x=80, y=90)


def percentage_calc():
    global i, operation
    n1 = e.get()
    i = int(n1)
    operation = "percent"
    e.delete(0, END)


button = Button(window, text="%", width=5, command=percentage_calc)
button.place(x=150, y=90)


def divide():
    global i, operation
    n1 = e.get()
    i = int(n1)
    operation = "div"
    e.delete(0, END)


button = Button(window, text="/", width=5, command=divide)
button.place(x=220, y=90)


def multiply():
    global i, operation
    n1 = e.get()
    i = int(n1)
    operation = "mul"
    e.delete(0, END)


button = Button(window, text="*", width=5, command=multiply)
button.place(x=290, y=90)


def minus():
    global i, operation
    n1 = e.get()
    i = int(n1)
    operation = "sub"
    e.delete(0, END)


button = Button(window, text="-", width=5, command=minus)
button.place(x=360, y=90)


def add():
    global i, operation
    n1 = e.get()
    i = int(n1)
    operation = "add"
    e.delete(0, END)


button = Button(window, text="+", width=5, command=add)
button.place(x=10, y=120)


def equal():
    global i, operation
    n2 = int(e.get())
    e.delete(0, END)

    if operation == "add":    
     e.insert(0, i + n2)
    elif operation == "sub":
        e.insert(0, i - n2)
    elif operation == "mul":
        e.insert(0, i * n2)
    elif operation == "div":
        if n2 != 0:
            e.insert(0, i / n2)
        else:
            e.insert(0, "Error")
    elif operation == "percent":
        e.insert(0, (i / 100) * n2)


button = Button(window, text="=", width=5, command=equal)
button.place(x=360, y=60)


def invertedcommasopen():
    e.delete(0, END)


button = Button(window, text="(", width=5, command=invertedcommasopen)
button.place(x=80, y=120)


def invertedcommasclose():
    e.delete(0, END)


button = Button(window, text=")", width=5, command=invertedcommasclose)
button.place(x=150, y=120)


def clear():
    e.delete(0, END)


button = Button(window, text="Clear", width=5, command=clear)
button.place(x=10, y=150)

##Main Loop
window.mainloop()
