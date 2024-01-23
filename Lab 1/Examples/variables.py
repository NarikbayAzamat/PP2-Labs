#1
x = 5
y = "John"
print(x)
print(y)

#2
x = 4       # x is of type int
x = "Sally" # x is now of type str

#3
x = str(3)   # x will be '3'
x = int(3)   # x will be 3
x = float(3) # x will be 3.0

#4
x = "John"
# is the same as
x = 'John'

#5
a = 4
A = "Sally"
#A will not overwrite a

#6
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John" # camel case

MyVariableName = "John" # pascal case

my_variable_name = "John" # snake case

#7
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#8
x = y = z = "Orange"
print(x)
print(y)
print(z)

#9
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#10
x = "Python is awesome"
print(x)

#11
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#12
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#13
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#14
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#15
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)