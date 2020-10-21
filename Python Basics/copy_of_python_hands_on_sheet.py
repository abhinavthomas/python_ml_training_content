print("Hello World!!")

age = 20
if age < 17:
  print("Can't have a DL yet!!")
else:
    print("OK, can have a DL.")

age = int(input("User age:"))
if age < 17:
  print("Can't have a DL yet!!")
else:
    print("OK, can have a DL.")

while input("Which is your favorite flower?") != "Rose":
  print("Try again !")
print("Of course it is !")

for chr in "string" :
  print(chr)

for elem in [1,4,5]:
  print(elem)

def celsius_to_fahrenheit(celsius):
  fahrenheit = celsius * 1.8 +32.0
  return fahrenheit
  print(fahrenheit)
celsius_to_fahrenheit(10)

def hello(name_man = "Bro", name_woman ="lady"):
 print("hello, " + name_man + " & " +name_woman + "!")
hello()
hello(name_woman= "Sis")
hello(name_man= "John", name_woman= "Mary")

import math
print(math.sqrt(4))

from math import sqrt
print(sqrt(4))

x = "Python is cool"
print(x[10])
print(x[2:6])
print(x[10:14])
print(len(x))
print(x + "?")
print(x.upper())
print(x.replace("c", "k"))
z = x.split(" ")
print(z)
print(",".join(z))
y= x.split("o")
print(y)
print(",".join(y))

x = [1,2,3,4]
print(x)
x[0] = 4
print(x)
x.append(5)
print(x)
print(x[3])

x = ["Python", "is", "cool"]
print(x)
x.sort()
print(x)
y = x[1:2]
print(y)
z = len(x)
print(z)
a = x + ["?", "Please", "Think", "Python"]
print(a)
print(x)
print(x[2])
x[1] = "Hot"
print(x)
print(a)
a.remove("Python")
print(a)
print(x)
x.pop(1)
print(x)

[i*2 for i in [0,1,2,3,4] if i%2 == 0]

[i.replace("o", "i") for i in ["python", "is","cool"] if len(i)>=3]

x = (0,1,2, "tuples"," ")
print(x)
y = 0,1,2, "tuples", " "
print(y)
# x[0] = 8 #will give error

x = [0,1,2,0,0,1,2,2] #list
y = {0,1,2,0,0,1,2,2} #set (removes duplicates)
print(x)
print(y)
print(y & {1,2,3}) #intersection
print(y | {1,2,3}) #union
print(y - {1,2,3}) #difference

x = {"India": "New Delhi", "Germany": "Berlin", "Italy": "Rome"}
print(x)
print(x["India"])
x["Japan"] = "Tokyo"
print(x)

class Person :
  def __init__(self,first,last): 
    self.firstname = first
    self.lastname  = last 
  def describe(self):
    return self.firstname +  " " + self.lastname

P1 = Person("Guido", "Van Rossum")
print(P1.describe() )

class Person :
  def __init__(self,first,last): 
    self.firstname = first
    self.lastname  = last 
  def describe(self):
    return self.firstname +  " " + self.lastname

class Employee(Person) :
    def __init__(self,first,last, staffnum):
      Person.__init__(self, first, last)
      self.staffnum = staffnum
    def describe(self):
      return self.lastname +  ", " + str(self.staffnum)  

P1 = Employee("Guido", "Van Rossum", 123456)   
print(P1.describe() )