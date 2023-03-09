thislist=["apple","banana","cherry","mango"]
thislist[0]="guava"
print(thislist)

mylist=["guava","chickoo","straberry","grapes","pomogrenate"]
mylist[2:4]=("apple","banana")
print(mylist)

mylist1=["mercedes","audi","bmw","rr","tesla","suzuki"]
mylist1[3:5]=("honda","kia")
print(mylist1)

mylist2=["apple","banana","cherry"]
mylist2[1:2]=("blackcurrent","watermelon")
print(mylist2)

#Change the second and third value by replacing it with one value:
mylist3=["apple","banana","cherry"]
mylist3[1:3]=["chickoo"]
print(mylist3)

#Insert "watermelon" as the third item:
mylist4=["apple","guava","cherry"]
mylist4.insert(2,"grapes")
print(mylist4)

