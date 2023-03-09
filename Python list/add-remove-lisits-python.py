#To add an item to the end of the list, use the append() method: append method
mylist=["apple","banana","guava"]
mylist.append("orange")
print(mylist)

#The insert() method inserts an item at the specified index:
mylist2=["banana","watermelon","cherry"]
mylist2.insert(2,"berry")
print(mylist2)


"""
To append elements from another list to the current list, use the extend() method
Add the elements of tropical to thislist:
"""
tropical=["apple","banana","cherry"]
thislist=["melon","chickoo","berry"]
thislist.extend(tropical)
print(thislist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Add elements of a tuple to a list:
thislist=["apple","banana","cherry"]
thistuple=("kiwi","dragonfruit")
thislist.extend(thistuple)
print(thislist)

#Remove Items
#The remove() method removes the specified item.
thislist4=["apple","orange","chickoo"]
thislist4.remove("orange")
print(thislist4)

#The pop() method removes the specified index.
thislist5=["apple","grapes","guava","berry"]
thislist5.pop(0)
print(thislist5)

#Remove the last item:
thislist6=["apple","kiwi","guava","pineapple"]
thislist6.pop()
print(thislist6)

#Remove the first item:
thislist7=["apple","samsung","xiaomi","oneplus"]
del thislist7[0]
print(thislist7)


#Clear the list content:
thislist=["changa","ddu","bvm"]
thislist.clear()
print(thislist)



