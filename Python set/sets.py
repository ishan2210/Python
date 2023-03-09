#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
thisset={"apple","banana","chickoo","mango"}
print(thisset)

thisset={"guava","kiwi","dragonfruit","pineapple"}
print(len(thisset))

thisset={"apple","banana","guava"}
print(type(thisset))

#constructor
thisset=set(("grapes","papita","pomogrenate"))
print(thisset)

#add sets
thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

set1={"apple","banana","chickoo"}
set2={"berry","guava","cherry"}
set1.update(set2)
print(set1)

#add elements to a list of a set
thiset={"apple","grapes"}
mylist=["orange"]
thiset.update(mylist)
print(thiset)

thisset={"apple","grapes","berry"}
del thisset

#If the item to remove does not exist, discard() will NOT raise an error.
thisset={"chickoo","grapes","berry"}
thisset.discard("grapes")
print(thisset)


