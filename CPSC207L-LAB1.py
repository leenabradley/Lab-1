Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Leena
print("Hello, world")
Hello, world
print("Welcome to CPSC 207")
Welcome to CPSC 207
print(Hello\nWorld")
      
SyntaxError: unexpected character after line continuation character
print("Hello\nWorld")
      
Hello
World
print("How\nare\nyou?")
      
How
are
you?
print("Today","is","Wednesday")
      
Today is Wednesday
print("Today"+"is"+"Wednesday")
      
TodayisWednesday
>>> #print statement types what we input
...       
>>> #\n commands the statement to tab to the next line
...       
>>> #when you combine strings with the plus operation it runs all of the command together as a unit. As if you had added them all together.
...       
>>> print("a\nb\nc")
...       
a
b
c
>>> print("Hello"+"World")
...       
HelloWorld
>>> print("Hello\n"+"\nWorld!")
...       
Hello

World!
>>> 
>>> 123
...       
123
>>> 45
...       
45
>>> 6
...       
6
>>> print("123\n45\n6")
...       
123
45
6
>>> 1+2*3
...       
7
>>> (1+2)*3
...       
9
7/3
      
2.3333333333333335
7//3
      
2
7%3
      
1
22/4
      
5.5
22//4
      
5
22%4
      
2
3**2
      
9
2**3
      
8
# yes python follows the rules of operations
      
# one / mark divides, whereas // divedes but turns the fraction into an integer
      
# the % gives the value of the remainder from divison
      
# ** represents exponential values
      

======== RESTART: C:/Users/Leena/AppData/Local/Programs/Python/Python312/save.py =======
#prediction one will equal 2.5
      
#prediction two will equal 0
      
(4+3)//2
      
3
6%2
      
0
1+2*3**4
      
163
print("2+2=",2+2)
      
2+2= 4
Print("50 pounds is", 50*0.453592,"Kilograms")
      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    Print("50 pounds is", 50*0.453592,"Kilograms")
NameError: name 'Print' is not defined. Did you mean: 'print'?
print("50 pounds is",50*0.453592,"Kilograms")
      
50 pounds is 22.6796 Kilograms
