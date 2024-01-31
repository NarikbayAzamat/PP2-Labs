#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#6
tuple1 = ("abc", 34, True, 40, "male")

#7
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#8
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#9
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#10
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#11
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

#12
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#13
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#14
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#15
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#16
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) this will raise an error because the tuple no longer exists

#17
fruits = ("apple", "banana", "cherry")

green, yellow, red = fruits

print(green)
print(yellow)
print(red)

#18
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#19
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#20
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#21
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#22
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

#23
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#24
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)