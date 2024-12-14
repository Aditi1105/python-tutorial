# ## VARIABLES
#
# myint = 9
# print(myint)
#
# mystring = 'Aditi'
# print(mystring)
#
# mynum = 10e10
# print(mynum)
#
# myfloat = 20.5
# print(myfloat)
#
# myfloat = myint
# print(myfloat)
#
# myfloat= float(myint)
# print(myfloat)
#
# myfloat= int(myfloat)
# print(myfloat)
#
#
# print (type(mynum))
# print (type(mystring))
#
# print(myfloat + myint)
#
# #
# # ### BUILT IN FUNCTIONS
# #
#
# print(dir(__builtins__))
#
# print( 2 ** 10)
#
# print(pow(2,10) )
#
# print(len('ADITI'))
#
# print(help(max))
#
#
# print(max(1,3,4,5,76))
#
# ### BUILT IN MODULES
#
# import math
# print(math.sqrt(100))
#
# print(help(math.sqrt))
#
#
# print(dir(math))
#
#
# # ## PYTHON STRINGS
# #
# x = 'Hello Aditi'
# print(x)
#
# y = "     Hello World       "
# print(y)
#
# z = "Aditi's Desktop"
# print(z)
#
# a = 'Hello\'s world'    ##use backslash (escape character) if we use ' inside of ''
# print(a)
#
# b = 'hello '
# print(b.capitalize())
#
# c="HELLO"
# print(x.upper())
# print(y.lower())
#
# print(x[2])
#
# print(y[6])
#
# print(x[0:3])
# print(z[2:6])
# print(y.strip())
#
#
# print(x.islower())
# print(c.isupper())
# print(x.replace("H","J"))
# print(x.split(','))
#
# print(b * 10)
#
# print("aditi".capitalize())
#
# #
# # ##BOOLEAN AND COMPARISON AND LOGICAL OPERATOR
# #
# print(10 > 20)
# print(30 < 40)
#
# x = 20
# y = 30
# z = 40
#
# print(x >= y )
#
# print('hello' ==  "hello")
#
#
# print( x < y and y > z)
# print( x < y or y > z)
# print( not x > y)
#
#
# # ## IF ELSE STATEMENT
# #
# x = 100
# y = -3
# if x == 100:
#     print(" x is equal to :" ,x)
#
# if x != 10:
#     print(" x is not equal to :" ,x)
#
# if x != 10 or x > 0:
#     print(" x is not equal to :" ,x)
# print("finish")
#
# if y > 0:
#     print("x is positive")
# else:
#     print("x is negative")
#
#
# # ## NESTED IF ELSE
# #
# name = input("enter a name: ")
#
# if name == "Max":
#     print("Entered name is :", name)
# elif name ==" Leo":
#     print("Entered name is :", name)
# elif name == "riya":
#     print("Entered name is :", name)
# else:
#     print("The name entered is invalid")
#
#
# x = 10
# if x < 0:
#     print("x is negative")
# else:
#     print("x is postive")
#     if (x % 2) == 0:
#         print("x is even")
#     else:
#         print("x is odd")
#
#
# if x > 0:
#     print("x is postive")
#     if (x % 2) == 0:
#         print("x is even")
#     else:
#         print("x is odd")
# else:
#     print("x is Negative")
#
#
# ##Python Lists
#
# x = [1,1,34,5,67,75]
# print(x)
#
# print(x[4])
#
# y = ["Max",1 , 14.5, [3,2]]
# print(y[1])
# print(y[3])
# print(len(x))
# print(x.insert(2,"Tom"))
# print(x)
# print(x.remove(1))
# print(x)
#
# print(x.pop())
# print(x)
#
# z= [1,2,3,4,]
# del z
#
# z= [1,2,3,4,]
# z.clear()
# print(z)
#
# a =[1,4,6,8,9]
# a.sort()
# print(a)
# a.reverse()
# print(a)
#
# a.append(10)
# print(a)
# s= x.copy()
# print(s)
# a.append(10)
# print(a)
# print (a.count(10))
from tkinter.font import names


## TUPLES are immutables i.e can't be modify

# x = (1,2,3,4)
#
# print(x)
#
# print(x[0])
#
#
# print(x.count(3))
# print(len(x))
#
# y = (1,'aditi',3,6,7,4.5)
# print(y)
#
# z = x + y
# print(z)
#
#
# a = ('hi,') * 5
# print(a)
#
# print(max(x))
#
#
# del z
# print(z)


## SETS is an unorderd collection with no duplicate elements and no indexing, i.e.must be unique value in a set.

# A = {1,3,4,5,7,8,9,3}    ## it will remove the duplicate value from the set
# print(A)
#
#
# print(len(A))
#
# A.add(10)     ## it will only add the element in the set which is not present in the set,
# print(A)
#
# A.add(3)                ## if the element is already present it will not add the element
# print(A)                ## it will do nothing
#
# A.update([12,34,56,78])
# print(A)
#
# A.remove(12)
# print(A)
#
# #A.remove(11)           ## when we try to remove the element which is not in set it will throw an exception error
# #print(A)
#
# A.discard(34)
# print(A)
#
# A.discard(11)         ## when we try to remove the element which is not in set it will not throw any exception error
# print(A)
#
#
# A.pop()
# print(A)
#
# name ={'max', 'tom','richie'}
# name.clear()
# print(name)
#
# #del name
# #print(name)
#
# name = set (('max','tom','jack'))    ## set contructor
# print(name)
#
# ##convert list to set
# z = set(['max','jack','red'])
# print(z)
#
#
# B= {33,55,6,77,88,99,344,66,777,998,4,9}
#
# print(A | B )  # A or B
#
# print(A.union(B))
#
# print(A & B)
#
# print(A.intersection(B))
#
# print(A - B)   ## all elemnts which are in A but not in B
# print(B - A)   ## all elemnts which are in B but not in A
#
# print(A.difference(B))
# print(B.difference(A))
#
# print(A ^ B)
# print(A.symmetric_difference(B))
#
# print(B ^ A)
# print(B.symmetric_difference(A))
#
# print(A[0])  ## sets are not indexed
#
# dir(A)

## DICTIONARIES  associative list or map, list of pairs, key value pair

# D = {'name': 'max','age': 22, 'year': 2000}
# print(D)
#
# print(D['name'])
#
# E = {'name': 'Tom', 15:15, 12.1:12.1,True:True,(2,3):4}
# print(E)
#
# print(E [(2,3)])
#
# print(E[True])
#
# print(E[12.1])
#
# #print(E[100])
# print(len(E))
#
# print(D.get('name'))
#
# D['Surname'] = 'teaser'
# print(D)
# D.pop('Surname')
# print(D)
#
# # E.clear()
# # print(E)
# #
# # del E
# # print(E)
#
# D['name'] = 'Tom'
# print(D)
#
# D.update({'name': 'Raj'})
# print(D)
# print(D.keys())
# print(D.items())
# print(D.popitem())  ## remove key value pair which we added or updated



## SLICE
# a = [0,1,2,3,4,5,6,7,8,9]
# b = (0,1,2,3,4,5,6,7,8,9)
# c = '0123456789'
#
# x = slice (0,5)
# print(a[x])
# print(x)
#
# print(a[0:3])
# print(b[3:])
# print(b[:5])
# print(c[:])
# print(c[3:6])
#
#
# print(a[0:9:2])
# print(a[0:9:3])
# print(a[::4])
#
# print(c[-1])   ## negative number index starts from the last value with -1
# print(c[-9])
#
# print(a[::-1])  ## -1 is used to give the list in reverse
# print(a[1::-1])
# print(a[:-3:-1])
# print(a[-2::-1])
# print(a[-2::-1])


## WHILE LOOP

# i = 0
# while i < 5:
#     print("the value of i is :", i)
#     i+=1  ## i = i +1
# else:
#     print("Finished The execution")
#
#
# num = 1
# sum = 0
# print("Enter a number. Please enter(0) to exit")
# while num != 0:
#     num= float (input("Enter a number"))
#     sum = sum + num
#     print("Sum:", sum)
# else:
#     print("Number is zero, exit")
#
#
# N = 10
# Sum = 0
#
# # This loop will run forever
# while True:
#     Sum += N
#     N -= 1
#
#     # the below condition will tell the loop to stop
#     if N == 0:
#         break
#
# print("Sum of First 10 Numbers is", Sum)
## FOR LOOP

# a = [0,1,2,3,4,5,6,7,8,9]  # list
# b = (0,1,2,3,4,5,6,7,8,9)  # tuple
# c = {0,1,2,3,4,5,6,7,8,9}  # set
# d = '0123456789'   # string
# e = {'name': 'Tom', 'age': 23}   # dictionary
#
# for x in a:
#     print(x)
#
# for x in b:
#     print(x)
#
# for x in c:
#     print(x)
#
# for x in d:
#     print(x)
#
# for x in e.keys():
#     print(x)
#
# for x in e.values():
#     print(x)
#
# for key, value in e.items():
#     print(key, " ", value)
#
# for x in range(6):
#     print(x)
# print()
#
# for x in range(2,6):
#     print(x)
# print()
#
# for x in range(2,30,3):
#     print(x)
# else:
#     print("Finished")


## Break and Continue
# a = [0,1,2,3,4,5,6,7,8,9]
# for x in a:
#     if x == 3:
#         break
#     print(x)
# print()
#
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i +=1
# else:
#     print("Finished The execution")
#
#
# for x in a:
#     if x == 3:
#         continue
#     print(x)
# print()
#
# i = 0
# while i < 5:
#     if i == 3:
#         continue
#     print(i)
#     i +=1
# else:
#     print("Finished The execution")
#
# i = 0
# while i < 5:
#     i +=1
#     if i == 2:
#         continue
#     print(i)

## FUNCTIONS  is  a group of statements within a program that perform specific task

# def sum(arg1,arg2):
#     if type(arg1) != type(arg2):
#         print("Please give the arguments of same type")
#         return
#     return(arg1 + arg2)
#
# a = sum(12,34)
# print(a)
# print(sum("Hello","World"))
# print(sum(12.44,45.66))
# print(sum("Hello",15))
#

## Default Arguments

# def student(name= 'Unknown name',age = 0):
#     print("name:", name)
#     print("age:", age)
#
# student("Tom",22)
#
# print()
# ## * argument
#
# def student(name,age,*marks):
#     print("name:", name)
#     print("age:", age)
#     print("marks:",marks)   ## this will give output as tuple
#     for x in marks:         ##using for loop will give out as separately
#         print(x)
#
#
# student("Tom",22, 10,20,45,55,66)
#
# print()
# ## ** argument
# def student(name,age,**marks):       ## double asterik will consider it as a dictionary
#     print("name:", name)
#     print("age:", age)
#     for key,value in marks.items():
#         print(key,' ',value)
#
#
# student("Tom",22, maths=10,hindi=20,english=45,science=55,history=66)

## Classes and Object

# class car:
#     pass
#
#
# ford = car()
# honda = car()
# audi = car()
#
# ford.color = 'red'
# ford.speed = 220
#
# honda.color = 'white'
# honda.speed = 200
#
# print(ford.color)
# print(honda.speed)
#
# ford.color = 'blue'
# ford.speed = 100
#
# print(ford.color)
# print(ford.speed)
#
#
# print()
#
# class rectangle:
#     pass
#
# rect1 = rectangle()
# rect2 = rectangle()
#
# rect1.heigth = 10
# rect2.height = 20
#
# rect1.width = 20
# rect2.width = 30
# print(rect1.heigth * rect1.width)
# print(rect2.height * rect2.width)


## INIT AND SELF
# class car:
#     def __init__(self,speed,color):
#         print(speed)
#         print(color)
#         self.speed = speed
#         self.color = color
#         print("Init is called")
#
#
# ford = car(200, 'white')
# honda = car(300,'red')
# audi = car(220,'black')
#
# print()
# print(ford.color)
# print(honda.speed)
#
#
# print()
#
#
#
# class rectangle:
#     def __init__(self,height,width):
#         self.height = height
#         self.width  = width
#
#
# rect1 = rectangle(20,22)
# rect2 = rectangle(10,12)
#
#
# print(rect1.height * rect1.width)
# print(rect2.height * rect2.width)

## Multiple Constructors

# class Hello:
#     def __init__(self):pass
#     def __init__(self,name):pass ## not possible to provide multiple init method and the init
#     # which we will provide at the last will be valid and other will be overwritten by the last init
#
#
# hello = Hello()


# class Hello:
#     def __init__(self,name):pass
#     def __init__(self):pass
#
#
# hello = Hello('name')


# class Hello:
#     def __init__(self,name= 'tom'):pass
#     ## default init agrument value
#
# hello = Hello()
# hello = Hello('name')
#
#
# class Hello:
#     def __init__(self,*args):pass
#     ## default init agrument value
#
# hello = Hello()
# hello = Hello('name','ah','ee')
#
# class Hello:
#     def __init__(self,**kwargs):pass
# hello = Hello()
# hello = Hello(name = 'tom')
#
#
# class Hello:
#     def __init__(self,name):    ## it is not necessary to provide all the arguments in the init
#         # we can provide inside the init with value
#         self.name = name
#         self.age = 10
#
# hello = Hello('name')

## ENCAPSULATION

class car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color

    def set_speed(self,value):
        self.__speed = value  ## __ is used to private the variable which means it is not used publicy or can't be overwrotten once assigned

    def get_speed(self):
        return self.__speed

    def set_color(self,value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = car(200, 'white')
honda = car(300,'red')
audi = car(220,'black')

ford.set_speed(220)
ford.__speed = 400
print()
print("speed of ford:", ford.get_speed())
# print(ford.color)


class rectangle:
    def __init__(self,height,width):
        self.__height = height
        self.__width  = width
    def set_height(self,value):
        self.__height = value

    def get_height(self):
        return self.__height

    def set_width(self,value):
        self.__width = value

    def get_width(self):
        return self.__width
    def area(self):
        return self.__height * self.__width

rect1 = rectangle(20,22)
rect2 = rectangle(10,12)

rect1.set_width(10)
rect1.set_height(20)
rect2.set_width(40)
rect2.set_height(30)
print("area of rectangle 1:", rect1.area())
print("area of rectangle 2:",rect2.area())


##  Private methods

class Hello:
    def __init__(self,name):
        self.a= 10
        self._b=20
        self.__c=30

    def public_method(self):
        print(self.a)
        print(self.__c)
        print('public')
        self.__private_method()

    def __private_method(self):
        print('private')

hello = Hello("name")
print(hello.a)
hello.public_method()
hello.__private_method()   ## we cant use the private method outside the class, will give error




## INHERITANCE -> classes in python can be extended to create a new class having
# characteristics of the base class
## two classes are these subclass and superclass
# subclass inherits the members of the super class and can add its own members

class polygon:
    __width = None
    __height = None
    def set_values(self,width,height):
        self.__width= width
        self.__height=height

    def get_width(self):        ## define this publicly so that we can access
        return self.__width         # the private members width and height in subclass

    def get_height(self):
        return self.__height

class rectangle(polygon):
    def area(self):
        return self.get_width() * self.get_height()

class triangle(polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2

rect = rectangle()
tria = triangle()
rect.set_values(3,4)  ## superclass
tria.set_values(30,50)  ## superclass

print("area of rectangle:", rect.area())   ## we cannot access the private members of superclass in subclass
## so we can define the another def in superclass with public def so that we can access in subclass
print("area of triangle:",tria.area())

## SUPER Keword
class parent:
    def __init__(self,name):
        print("parent __init name: ",name)

class parent2:
    def __init__(self,name):
        print("parent2 __init name: ",name)

class Child(parent,parent2):
    def __init__(self):
        print("child __init name: ")
#        super().__init__('max')
        parent.__init__(self,'Tom')
        parent2.__init__(self,'Max')

child = Child()
print(Child.__mro__)


## COMPOSITION


class salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.obj_Salary=salary(pay,bonus)   # define Salary from class salary

    def total_salary(self):
        return self.obj_Salary.annual_salary()

emp=Employee("Max",25,15000,10000)
print(emp.total_salary())
#
#
#
# ##Aggregation
class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.obj_Salary=salary  # define Salary from class salary

    def total_salary(self):
        return self.obj_Salary.annual_salary()
salary = Salary(15000,10000)
emp=Employee("Max",25,salary)
print(emp.total_salary())


#Abstract Class
from abc import ABC, abstractclassmethod, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side
#shape = Shape()  # this will give error bcz we cant use object of an abstract class
square = Square(5)
print(square.area())
print(square.perimeter())
#


## Exception handling

result = None
a = float(input("Number 1"))
b = float(input("Number 2"))
try:
    result = a/b
except Exception as e :
    print("Error :",e)

print("Results are = ", result)
print("End")


result = None
a = float(input("Number 1"))
b = float(input("Number 2"))
try:
    result = a/b
except ZeroDivisionError as e :
    print("Error :",e)

print("Results are = ", result)
print("End")


result = None
a = (input("Number 1"))
b = float(input("Number 2"))
try:
    result = a/b
except TypeError as e :
    print("Error :",e)

print("Results are = ", result)
print("End")


#try else finally

result = None
a = float(input("Number 1"))
b = float(input("Number 2"))
try:
    result = a/b
except ZeroDivisionError as e :
    print("Error :",type(e))

except TypeError as e :
    print("Error :",type(e))

else:   ## whenever our code doesn't throw any exception, it will be exceuted
    print("In else")

finally:  ##always executed if code throws error or doesn't throe error
    print("executed finally")

print("Results are = ", result)
print("End")

## we can't use else and finally without exception but we can use finally without else and except



## if name


def add(a,b):
    return a + b
print(__name__)
if __name__ == "__main__":
    print(add(10,20))



## ITERATOR

class ListIterator:

    def __init__(self,list):
        self.__list=list
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index +=1
        if self.__index == len(self.__list):
            raise StopIteration
        return self.__list[self.__index]

a = [1,2,3,4,6,7,9]
mylist = ListIterator(a)

it = iter(mylist)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for i in it:
    print(i)

##Generators, yield pausing the function and saving that function,
# instead of using iter method, way simpler than iterators, it will give stopiteration error itself
# in generators iterators are automatically implemented
# save the status of iterator

def my_func():
    n= 1
    for i in range(5):
        print("value if i:",i)
        yield i
    print("value of n 1:", n)
    yield n
    n +=1
    print("value of n 2:", n)
    yield n
    n +=1
    print("value of n 3:", n)
    yield n
x = my_func()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
#
def list_iterator(list):
    for i in list:
        yield i
a = [1,2,3,4,6,7,9]
mylist = list_iterator(a)
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
for x in mylist:
    print(x)

## Command Line Arguments

import argparse
if __name__  == '__main__':
    parser = argparse.ArgumentParser(   ##description is the optional parameter of argumentparser
        description="my math script"
    )
 #    Add the parameters positional
 #    parser.add_argument('num1',help="Number 1",type= float)
 #    parser.add_argument('num2',help="Number 2",type= float)
 #    parser.add_argument('operation',help="provide")

    #Add the parameters Optional
    parser.add_argument('-n','--num1',help="Number 1",type= float)
    parser.add_argument('-i','--num2',help="Number 2",type= float)
    parser.add_argument('-o','--operation',help="provide",default='+')
#
# #Parse the arguments
    args = parser.parse_args()
    print(args)
    result = None
    if args.operation == "+":
        result = args.num1 + args.num2
    if args.operation == "-":
        result = args.num1 - args.num2
    if args.operation == "*":
        result = args.num1 * args.num2
    if args.operation == "pow":
        result=pow(args.num1,args.num2)

    print("Results:", result)




##LAMBDA FUNCTIONS

# def double (x):
#     return x*2
# def add(x,y):
#     return x+y
# def product(x,y,z):
#     return x*y*z


#lambda is equivalent to the above defined def
double = lambda x: x*2
add = lambda x,y : x+y
product = lambda x,y,z : x*y*z

print(double(10))
print(add(10,30))
print(product(10,30,20))
#
# #filter,reduce and map
mylist= [2,3,4,5,6,7,8]
mylist2= [1,3,7,9,3,2,5]
a= map(lambda x : x * 2,mylist)
print("List 1")
print(list (a))
#
b= map(lambda x,y : x +y ,mylist,mylist2)
print("list 2")
print(list (b))
#
#
# ##filter
c= filter(lambda x : x%2 == 0,mylist)
print("list 3")
print(list (c))
#
d= filter(lambda x : True if x>=5 else False ,mylist2)
print("list 4")
print(list (d))
#
# ##reduce sum of two elements and then add that to the another element of list  2+3= 5, 5+4=9,9+5...and o on
from functools import reduce
e = reduce(lambda x,y : x+y,mylist)
print("list 5")
print(e)


##CLOSURES and NESTED FUNCTIONS
#NESTED FUNCTION
def outerFunction(text):
    def innerfunction():
        print(text)
    innerfunction()

outerFunction("hello")


## NESTED FUNCTION
def pop(list):
    def get_last_item(my_list):
        return my_list[len(list) - 1]

    list.remove(get_last_item(list))
    return list

a= [1,2,3,4,5,6]
print(pop(a))
print(pop(a))
print(pop(a))
#


##CLOSURES is able to remember the value which are declared outside the function
def outerFunction(text):
    def innerfunction():
        print(text)
    return innerfunction

a = outerFunction("hello")
del outerFunction
a()

def nth_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of

square = nth_power(2)
print(square(2))
print(square(3))
print(square(4))
print(square(5))

cube =nth_power(3)
print(cube(2))
print(cube(3))
print(cube(4))
print(cube(5))

##Decorators wraps a function and modify its behavior in one way or another without changing the source of code
def decorator_func_X(func):
    def wrappeer_func():
        print('X' * 20)
        func()
        print('X' * 20)

    return wrappeer_func

def decorator_func_Y(func):
    def wrappeer_func():
        print('Y' * 20)
        func()
        print('Y' * 20)

    return wrappeer_func

@decorator_func_Y
@decorator_func_X

def say_hello():
    print('Hello world')

hello = decorator_func_X(decorator_func_Y(say_hello))
hello()

say_hello()

def decorator_divide(func):
    def wrapper_func(a,b):
        print('divide' , a , 'and', b)
        if b==0:
            print('division with zero is not allowed')
            return
        return a/b
    return wrapper_func

@decorator_divide
def divide(x,y):
    return x/y

print(divide(15,0))

from time import time
def timimg(func):
    def wrapper_func(*args,**kwargs):
        start = time()
        print("start time:",start)
        result = func(*args,**kwargs)
        end= time()
        print("end time:",end)
        print('Elasped Time: {}'.format(end-start))
        return result

    return wrapper_func

@timimg
def my_func(num):
    sum=0
    for i in range(num+1):
        sum +=1
    return  sum

print(my_func(20000000))





##Operator Overloading
import math
class Circle:
    def __init__(self,radius):
        self.__radius =radius

    def setradius(self,radius):
        self.__radius =radius

    def getradius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, circle_object):
        return  Circle(self.__radius + circle_object.__radius)
    def __lt__(self, circle_object):
        return  (self.__radius < circle_object.__radius)
    def __gt__(self, circle_object):
        return  (self.__radius > circle_object.__radius)
    def __str__(self):
        return "Circle area = " + str(self.area())

c1 = Circle(12)
c2 = Circle(13)
c3 = c1 + c2

print(c1.getradius())
print(c2.getradius())
print(c3.getradius())

print(c1 < c2)
print(c1 > c2)
print(c3 > c2)

print(str(c1))
print(str(c2))
print(str(c3))

















