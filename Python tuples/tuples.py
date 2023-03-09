#Tuples are used to store multiple items in a single variable.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
thistuple=("apple","banana","cherry","mango")
print(thistuple)

thistuple=("apple","banana","cherry","mango")
print(len(thistuple))

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple1=("apple",)
print(type(thistuple1))

thistuple1=("apple")
print(type(thistuple1))

#It is also possible to use the tuple() constructor to make a tuple.
thistuple=tuple(("apple","banana","cherry"))
print(thistuple)

