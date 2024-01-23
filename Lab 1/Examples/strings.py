#1
a = "Hello, World!"
print(a[1])

#2
for x in "banana":
    print(x)

#3
a = "Hello, World!"
print(len(a))

#4
txt = "The best things in life are free!"
print("free" in txt)

#5
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#6
txt = "The best things in life are free!"
print("expensive" not in txt)

#7
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

#8
b = "Hello, World!"
print(b[2:5])

#9
b = "Hello, World!"
print(b[:5])

#10
b = "Hello, World!"
print(b[2:])

#11
b = "Hello, World!"
print(b[-5:-2])

#12
a = "Hello, World!"
print(a.upper())

#13
a = "Hello, World!"
print(a.lower())

#14
a = " Hello, World! "
print(a.strip())

#15
a = "Hello, World!"
print(a.replace("H", "J"))

#16
a = "Hello, World!"
b = a.split(",")
print(b)

#17
a = "Hello"
b = "World"
c = a + b
print(c)

#18
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#19
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#20
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#21
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#22
txt = "We are the so-called \"Vikings\" from the north."
