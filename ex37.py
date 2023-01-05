'''import calendar as c #as creates an alias
from datetime import time #from imports only a section of a module

x = time(hour=15) #using time from datetime to select an hour
print(x)

print(c.month_name[1])#month_name is a variable pulled from calendar

lettuce = "romaine"

if "romaine" and "ro" in lettuce:
    print("YES")
print(lettuce)

for i in range(9):
    if i > 3:
        break
print(i)

greeting = "hello"

"""assert is used for debugging whether a condition is true. A comma 
can be added with a message after to return what the true statement 
should be"""
assert greeting == "goodbye" , "greeting should be 'hello'"'''

"""class Man:
    name = "Colin"
    age = 30
    height = f"6'2\""
    weight = 165
    sex = "Male"
    city = "Mesa"

def asl():
    asl = Man()
    print(f"{asl.age}/{asl.height}/{asl.sex}/{asl.city}.")

asl()"""

#del Man.height 
# del can be used to delete objects

x = lambda a, b, c : a * b / c
y = lambda a, b : a + b
print(x(3, 5, 2)) 
print(y(3, 5))






