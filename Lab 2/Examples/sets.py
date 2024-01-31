#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2 Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#3 True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#4
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#5
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#6
set1 = {"abc", 34, True, 40, "male"}

#7
myset = {"apple", "banana", "cherry"}
print(type(myset))

#8
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#9
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#10
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#11
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#12 To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#13
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#14 If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#15
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#16 Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#17
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#18
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) - error

#19
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#20
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#21
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#22
#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#23
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#24
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#25
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#26
#Return a set that contains the items that only exist in set x, and not in set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#27
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#28
#Return True if no items in set x is present in set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#29
#Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#30
#Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)