# python-assignments
All Python Assignments 
From the Basics of adding and finding #true for value, "strings", Boolean, #change index value,#range: seperated by a Colon':#append: to add at the end,#insert value at index (index,'value')
#remove value based on (value),#delete del:and index,#TUPLES: Cannot change but reassign,#modification operations are not allowed
#in operator true or false : Boolean value,#strings are collection type: index based,#lamda: expressionnumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
answer = set(filter(even, numbers))
answer = tuple(filter(even, numbers))
answer = list(filter(even, numbers))
print(answer)
#filter(function,iterable)
number = (1, 2, 3, 4, 5)
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
#dict={key:'value',key:'value1'},#true false in operator, if else statement Doubt Cleared on chat
elif statements##loops
  #for loop for known number of iterations or times
  #while loop until the condition is met
#n=10
#i=0
#while i<n:
# print(f'Hello,{i}')
#i+=1 != is not,#Parameters
#Function can have 0 or more parameters, any type or mixed eg. def(define for variables) add_numbers(num1,num2):
#will return the value eg def add_numbers(num1,num2):
#return num1+num2, calling a function defined once and called mutiple times,eg result=add_numbers(1,2) print(result), Output:3,also result=add_numbers(5,7) print(result)# output: 12
#def add_numbers(a,b):
#return(a+b)
#result=add_numbers(1,2)
#print(result),## Control Flow statements# == is comparison and = is assignment,#while loops#write once and run multiple times need to introduce break
#condition True or False Execute Code and repeats the process#break and continue statemnt,##For in Loop item in collection execute code using item  [] bracket to be used

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
  position = 0 with solution to the problem
  #global position #Access keyword outside the function



position=0
#def move_player(by_amt):
 # global position
  #position += by_amt
  #print(position)

#move_player(5)
## Objects: code with Variables and Functions
## Classes: blueprints for creating objects defining variables and functions
## Inheritance: allows new objects to take on the properties of existing objects
## Polymorphism: refers to the way in which object classes can share the same method names
## Encapsulation: refers to the bundling of data and methods within a single unit
#class Construc:
 # x = 0
  #def __init__(self):  # Corrected: double underscores and colon
   # print("Construced")
   ##"__" hide attributes, '' shows attributes
print(dir(s))

#import re
#regular #first 5  characters are taken into account,expressions,regex,strings, to validate input
import re
##findall 
  #findall(pattern,String,Flags)
  ## Search = Find String 
##Match= First 5 characters
# replace Words in a String : sub, Flags=0,1
## sub(pattern,repl,string,count,flags) repl: replacing word
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
learned about tkinter and made a calculator 
(help taken on chat )
## Abstraction: refers to the process of hiding the internal details of an object or class from the user
