#1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#5
list1 = ["abc", 34, True, 40, "male"]

#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#8
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#9
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#13
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#14
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#15
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#16
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#17
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#18
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#19
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#20
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#21
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#22
'''
The remove() method removes the specified item.
If there are more than one item with the specified value, the
remove() method removes the first occurance
'''
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#23
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#24
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#25
# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#26
# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

#27
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#28
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#29
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#30
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#31
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#32
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#33
list2 = [x for x in range(10)]

#34
newlist = [x.upper() for x in fruits]

#35
newlist = [x if x != "banana" else "orange" for x in fruits]

#36
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#37
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#38
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#39
#Sort the list based on how close the number is to 50:
def myFunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myFunc)
print(thislist)

#40
#So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#41
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#42
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#43
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#44
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#45
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

#46
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
