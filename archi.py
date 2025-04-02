#true for value, "strings", Boolean
enemy_position = [5, 10, 15]
print(enemy_position)
print(enemy_position[2])
print(len(enemy_position))
#change index value
enemy_position[2] = 6
print(enemy_position)
#range: seperated by a Colon':'
print(enemy_position[0:2])
#append: to add at the end
enemy_position.append(25)
print(enemy_position)
#insert value at index (index,'value')
enemy_position.insert(1, 9)
print(enemy_position)
#remove value based on (value)
enemy_position.remove(6)
print(enemy_position)
#delete del:and index
del (enemy_position[2])
print(enemy_position)

#true for value, "strings", Boolean
enemy_position = [5, 10, 15]
print(enemy_position)
print(enemy_position[2])
print(len(enemy_position))
#change index value
enemy_position[2] = 6
print(enemy_position)
#range
print(enemy_position[0:2])
#append
enemy_position.append(25)
print(enemy_position)
#insert value at index
enemy_position.insert(1, 9)
print(enemy_position)
#remove value based on index
enemy_position.remove(6)
print(enemy_position)
#delete
del (enemy_position[2])  #add a
print(enemy_position)
#TUPLES: Cannot change but reassign
high_score = ('Name', 120)
print(high_score)
high_score = ('Sund', 180)
print(high_score)
#print index based result[]
name = high_score[0]
print(name)
#modification operations are not allowed
#in operator true or false : Boolean value
print('name' in high_score)
#strings are collection type: index based
print(name[0])
print(name[0:3])


#lamda: expression
def add(a, b):
  return a + b


def fun(a, b):
  return a + b


res = fun(2, 3)
print(res)
lambda a, b: a + b
print(res)


def even(a):
  return a % 2 == 0


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
answer = set(filter(even, numbers))
answer = tuple(filter(even, numbers))
answer = list(filter(even, numbers))
print(answer)
#filter(function,iterable)
number = (1, 2, 3, 4, 5)


def square(a):
  return a**2


solution = list(map(square, number))
#map(funcion,iterable)
#a=(1,2,5)
#print(a)
#lists
#name , assisgnment operator ,text or values
#name =[5, 'name','true', 'string']
#enemy_position = [5,10,15]
#print(enemy_position)
#index
#print(enemy_position[2])
#len=length
#print(len(enemy_position))
# Dictonaries{}
#dict={key:'value',key:'value1'}
actions = {"r": 1, "l": -1}
print(actions)
print(actions["r"])
print(actions.get("h"))
#update key values
actions["r"] = 2
actions["a"] = 4
print(actions)

print(actions.items())
print(actions.keys())
print(actions.values())
#del(actions["r"])
del (actions["a"])
print(actions)

actions.pop("r")
print(actions)
#true false in operator
print("l" in actions)
#Robot_nav.py
mark = int(input('Enter Mark:'))
if mark >= 7:
  print('Grade A')
  print('Stop')
if mark > 10:
  print('Grade A+')

  total_marks = 100
  marks_obtained = int(input('Provide test Mark:'))
  if marks_obtained >= 60:
    print("Pass")
  else:
    print("Fail")
  percentage_marks = marks_obtained / total_marks * 100
  print(percentage_marks)
  print('End')
  marks = int(input('enter Test Marks:'))
  if marks < 5:
    print('Grade F')
  elif marks >= 5 and marks < 10:
    print("Grade E")
  elif marks >= 10 and marks < 15:
    print('Grade D')
  elif marks >= 15 and marks < 20:
    print('Grade C')
  elif marks >= 20 and marks < 25:
    print('Grade B')
  elif marks >= 25 and marks < 30:
    print('Grade A')
  else:
    print('Grade A+')

  print('End')
  ##loops
  #for loop for known number of iterations or times
  for i in range(5):
    print(f"hello,{i}")
  for i in range(2, 5):
    print("Hi")
    print(list(range(2, 5)))
#while loop until the condition is met
#n=10
#i=0
#while i<n:
# print(f'Hello,{i}')
#i+=1 != is not
'''
user_input=input('Enter True or False(either T or F'))
while user_input!="T"and user_input!="F":
  user_input=input('Enter True or False(either T or F')
  print(f"Said: {user_input}")'''

while True:
  user_input = input('Say (T or F)')
  if user_input == "T" or user_input == "F":
    break
  print('Said:{user_input}')

Marks = int(input('Enter Marks:'))
if Marks >= 7 and Marks < 11:
  print('A')
elif Marks >= 6 and Marks < 8:
  print('B')
elif Marks >= 5 and Marks < 7:
  print('C')
elif Marks >= 1 and Marks < 3:
  print("F")
else:
  print('Wrong Marks')


#Parameters
#Function can have 0 or more parameters, any type or mixed eg. def(define for variables) add_numbers(num1,num2):
#will return the value eg def add_numbers(num1,num2):
#return num1+num2, calling a function defined once and called mutiple times,eg result=add_numbers(1,2) print(result), Output:3,also result=add_numbers(5,7) print(result)# output: 12
#def add_numbers(a,b):
#return(a+b)
#result=add_numbers(1,2)
#print(result)
def get_random_secret(a, b):
  if a >= 0 and b <= 100:
    print('True')
  elif a < 0 and b > 100:
    print('False')


a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
get_random_secret(a, b)


## Control Flow statements# == is comparison and = is assignment
def move(direction):
  if direction == "right":
    print("Moving right")
  elif direction == "left":
    print("Moving left")
  elif direction == "Centre":
    print("Moving centre")
  else:
    print("Invalid direction")


move('Centre')
move('right')
move('left')
#while loops#write once and run multiple times need to introduce break
#condition True or False Execute Code and repeats the process#break and continue statemnt
position = 0
end_position = 8
enemy_positionn = 6

while position < end_position:
  position += 1
  if position == enemy_positionn:
    print("Close")
    break
  if position == end_position:
    print("The End")

print(position)

##For in Loop item in collection execute code using item  [] bracket to be used

"""enemy_positions = [5, 10, 15]
for enemy_positions in enemy_positions:
  enemy_positions += 1
  print(enemy_positions)
  break

for i in range(0, 5):
  print("hello")
  ##Functions one function to one purpose , big function split in smaller ones
  #def function_name(parameter):
  #code
  # return value(function_name)
  position = 0

  def move_player(position):
    #global position #Access keyword outside the function
    position += 1
    print(position)

  move_player(position)
"""
#global position #Access keyword outside the function



position=0
#def move_player(by_amt):
 # global position
  #position += by_amt
  #print(position)

#move_player(5)

def move_player(by_amt,position):

   position += by_amt  ## atleast one value to be provided
   print(position)
move_player(10,position)
## return  statements

def move_player1(position, by_amt):
  position+=by_amt
  return position  ## can use without value 

position=move_player1(position,5)
position=move_player1(position,5)
print(position)


by_amt=0
def move_player2(position, by_amt):
  by_amt+=position
  return by_amt  ## can use without value 

by_amt=move_player2(1,by_amt)
by_amt=move_player2(2,by_amt)
print(by_amt)
## Objects: code with Variables and Functions
## Classes: blueprints for creating objects defining variables and functions
## Inheritance: allows new objects to take on the properties of existing objects
## Polymorphism: refers to the way in which object classes can share the same method names
## Encapsulation: refers to the bundling of data and methods within a single unit
## Abstraction: refers to the process of hiding the internal details of an object or class from the user

class GameObject: ## Nameing Rule for Class 

  def __init__(self, name, x_pos, y_pos):  ## Initializer function to hold values for the class
    self.name = name ##variables
    self.x_pos = x_pos ##variables
    self.y_pos=y_pos ##variables

  def move(self, by_x_amount, by_y_amount):
    self.x_pos += by_x_amount ## properties
    self.y_pos+= by_y_amount

game_object=GameObject("Enemy",1,2)
print(game_object.name)
game_object.name="Enemy 1"
print(game_object.name)
print(game_object.x_pos)
print(game_object.y_pos)

game_object.move(2,5)
print(game_object.x_pos)
print(game_object.y_pos)

other_game_object=GameObject("Player",2,0)
print(other_game_object.name)
print(other_game_object.x_pos)
print(other_game_object.y_pos)



class Enemy(GameObject): 
 ##Inheritance
  def __init__(self, name, x_pos, y_pos, health):
    super().__init__(name, x_pos, y_pos) ##Inheritance;super class initializer
    self.health=health ##properties 

  def take_damage(self, amount):
    self.health-=amount
  def add_health(self,amount):
    self.health+=amount

game_object=GameObject("GameObject",1,2)
enemy=Enemy("Enemy",5,10,100)

print(game_object.name)
print(enemy.name)
enemy.take_damage(20)
print(enemy.health)

"""class Car:
  def __init__(self, X_pos, Y_Pos, Model, color1,color2):
    # Initialize the object's attributes here  
    self.Model="SUV"
    self.X_pos=X_pos
    self.Y_Pos=Y_Pos
    self.color1=color1
    self.color2=color2

  def color(self, red,blue):
    self.color1= red
    self.color2=blue

car=Car(1,2,3,"red","blue")
print(car.color1)
print(car.color2)
print(car.Model)
print(car.X_pos)"""

"""class GameObject: ## Nameing Rule for Class 

  def __init__(self, name, x_pos, y_pos):  ## Initializer function to hold values for the class
    self.name = name ##variables
    self.x_pos = x_pos ##variables
    self.y_pos=y_pos ##variables

  def move(self, by_x_amount, by_y_amount):
    self.x_pos += by_x_amount ## properties
    self.y_pos+= by_y_amount

game_object=GameObject("Enemy",1,2)
print(game_object.name)
game_object.name="Enemy 1"
print(game_object.name)
print(game_object.x_pos)
print(game_object.y_pos)

  """

#class Construc:
 # x = 0
  #def __init__(self):  # Corrected: double underscores and colon
   # print("Construced")
"""a=1
b=2
print(a+b)
print(int.__add__(a,b))"""
##Overloading Operator
class veggies:
  def __init__(self,carrot,beans):
   self.carrot=carrot
   self.beans=beans
  def __add__(self,other):
   carrot=self.carrot+other.carrot
   beans=self.beans+other.beans
   return veggies(carrot,beans)

veggies1=veggies(10,20)
veggies2=veggies(30,40)
veggies3=veggies1+veggies2
print(veggies3.carrot)
print(veggies3.beans)
class simple:

  def __init__(self):
    self.__value_1 = 1
    self.value_2 = 2

  def A1_(self):
    print("Apple")

  def B2_(self):
    print("Banana")


s = simple()
print(s._simple__value_1)
##"__" hide attributes, '' shows attributes
print(dir(s))

#import re
#regular #first 5  characters are taken into account,expressions,regex,strings, to validate input
import re
pattern="apple"
if re.match(pattern,"apple"):
 print("T")
else:
 print("F")

  #Match Function
  #match(pattern, String, Flags)
  import re

  pattern="apple"
  if re.match(pattern,"apple",flags=0):
    print("T")
  else:
    print("F")

  ##findall 
  #findall(pattern,String,Flags)
  pattern="apples"
  string=re.findall(pattern,"apples are red",flags=0)
  print(string)
#search(pattern,string,flags)
import re
pattern="apple"
if re.search(pattern,"apple"):
  print("T")
else:
  print("F")
## Search = Find String 
##Match= First 5 characters
# replace Words in a String : sub, Flags=0,1
## sub(pattern,repl,string,count,flags) repl: replacing word
import re
string="It is a Dog"
pattern="Dog"
print(re.sub(pattern,"Cat",string,count=0, flags=0))
#Characters and Character Sequence
# ^: matches the beginning of the string
# $: matches the end of the string
# .: matches any character
# *: matches zero or more occurrences of the preceding element
#\d: matches any digit
#\D: matches any non-digit
#\s: matches any whitespace character
#\S: matches any non-whitespace character
#\w: matches any word character
#+ : repeats characters one or  more time 
#? : repeats characters zero or one time
#{} : repeats characters a number of times
#[] : matches characters in a list
#| : matches either or
#(): marks start and end of a group resp
#[aeiou]: matches any of the characters in the list]
#[^xyz]: matches single character
#[a-z 0-9]: matches any character in the range

import re
string= "It is a dog"
pattern="do+"
print(re.findall(pattern,string))

##Step 1: Import tkinter
from tkinter import *
#Step 2: GUI Interaction
window = Tk()
#step 3: adding instruction/inputs
inp= Label(window, text="Hello World")
inp.pack()
#Step 4: Main Loop
window.mainloop()
from tkinter import Tk,mainloop
window=Tk()
window.title("Simple")#page title 
window.geometry("300x700")#dimentions
window.config(bg="red")# color
mainloop()
window.title("Simple")  #page title
window.geometry("500x500")  #dimentions
window.config(bg="White")  # color
frame1 = Frame(window, width=300, height=300, cursor="arrow")
frame2 = Frame(window, width=300, height=300, cursor="cross")
frame1.pack(side=TOP)  ##Always Pack
frame2.pack(side=BOTTOM)
button1 = Button(frame1, text="Button1", cursor="arrow", bg="red")
button2 = Button(frame2, text="Button2", cursor="cross",bg="blue")
button3=Button(frame1,text="Button3",cursor="circle",bg="green")
button1.pack()
button2.pack()
button3.pack()
mainloop()
import tkinter.messagebox
window = Tk()##GUI Interaction
tkinter.messagebox.showinfo("Hello", "Hello World")
tkinter.messagebox.showerror("Error", "Error")
tkinter.messagebox.askquestion(title="Question", message="Are you sure?")
question=tkinter.messagebox.askokcancel("Weather","Will it rain today?")
if question == True:
  print("Take an umbrella")
else:
  print("Sunny Day")

## Main Loop
window.mainloop()
## Adding inputs
window.title("Simple")
window.geometry("300x50")
label1=Label(window,text="Mail")
label2=Label(window,text="Password")
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
e1= Entry(window, width=20, bg="white",borderwidth=5)
e1.grid(row=0,column=1)
e2= Entry(window, width=20, bg="white",borderwidth=5)
e2.grid(row=1,column=1)
#mainloop()
window.mainloop()

window.title("Simple")
window.geometry("300x500")
label1=Label(window,text="Mail", bg='red', fg="Orange")
label2=Label(window,text="Password", bg='blue', fg="white")
label3=Label(window,text="word", bg='green', fg="white")
label4=Label(window,text="Pass", bg='violet', fg="white")
label1.pack(side=TOP,fill= "x" , expand=False)
label2.pack(side=BOTTOM,fill= "y" , expand=False)
label3.pack(side=LEFT,fill= "x" , expand=TRUE)
label4.pack(side=RIGHT,fill= "y" , expand=False)

window.mainloop()
def log_Entry():
  print('Logged in' )
button=Button(window,text="LOGIN", command=log_Entry,width=12,bg="Red", fg="white",font="BOLD 12",activebackground="Blue", activeforeground="White")
button.pack()
window.mainloop()   

menu=Menu(window)
file=Menu(menu,tearoff=0)     
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Close")
file.add_separator()
file.add_command(label="Exit", command=window.quit)
menu.add_cascade(label="File",menu=file)
window.config(menu=menu)
tkinter.messagebox.showinfo("Hello", "Hello World")
tkinter.messagebox.showerror("Error", "Error")
tkinter.messagebox.askquestion(title="Question", message="Are you sure?")
question=tkinter.messagebox.askokcancel("Weather","Will it rain today?")
if question == True:
  print("Take an umbrella")
else:
  print("Sunny Day")
  c=Canvas(window, width=500, height=500, bg='white')
  c.pack()
  c.create_line(0,0,500,500,width=5,fill="red",dash=(5,5))##add dash for dotted line
  c.create_line(0,500,500,0,width=5,fill="green")
  c.create_rectangle(150,150,300,300,fill="orange",outline="red",width=5)

  #window.geometry("500,500")#Method 1 use message
  #message= Message (window,text="Python")
  #message.pack()


  var=StringVar()## Method 2 use Label&3
  ent_var=StringVar() 

  def insert():
      result=ent_var.get()
      var.set(result)

  #message=Message(window,textvariable=var,relief="raised",padx=15,pady=15)#relief=Adding 2D border
  #var.set("Welcome")
  #message.pack()
  message=Message(window,textvariable=var,relief="raised",padx=25,pady=25)
  entry= Entry(window,textvariable=ent_var,width=20,bg="white",borderwidth=5)
  button=Button(window,text="Click",width=20,bg="red",fg="white",command=insert)
  message.pack()
  entry.pack()
  button.pack()
  check_box1 = IntVar()
  check_box2 = IntVar()
  check_box3 = IntVar()
  check_button_1 = Checkbutton(window,
                               text="English",
                               variable=check_box1,
                               onvalue=1,
                               offvalue=0,
                               height=5,
                               width=2)
  check_button_2 = Checkbutton(window,
                               text="Hindi",
                               variable=check_box2,
                               onvalue=1,
                               offvalue=0,
                               height=5,
                               width=2)
  check_button_3 = Checkbutton(window,
                               text="Marathi",
                               variable=check_box3,
                               onvalue=1,
                               offvalue=0,
                               height=5,
                               width=2)
  check_button_1.pack()
  check_button_2.pack()
  check_button_3.pack()

  window.mainloop()
button=Button(window, width=10, height=5, text="Start", bg="White", fg="Yellow", activebackground="Green",)
button.place(x=150,y=150)