#Convert the tuple into a list to be able to change it:
x=("apple","banana","chickoo","orange","melon")
y=list(x)

y[1]="berry"
x=tuple(y)
print(x)

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
tuple1=("apple","banana","chickoo","berry")
y=list(tuple1)
y.append("orange")
tuple1=tuple(y)
print(tuple1)

#Create a new tuple with the value "orange", and add that tuple:
thistuple=("apple","banana","cherry","chickoo")
x=("orange",)
thistuple += x
print(thistuple)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple
thistuple=("apple","banana","chickoo","orange","grapes")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)

#remove tuples completely
thistuple=("apple","banana","cherry","orange","berry")
del thistuple
print(thistuple)


