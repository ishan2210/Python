fruits=["apple","banana","cherry"]
for x in fruits:
  print(x)

  for x in "banana":
   print(x)


cars=["BMW","Mercedes","Audi"]
for x in cars:
    print(x)
    if x=="Mercedes":
     break

cars2=["KIA","Honda","Tata"]
for x in cars2:
    if x== "Honda":
     continue
    print(x)

for x in range(6):
 print(x)
else:
    print("Finally Finished")


for x in range(6):
    if x==3:
        break
    print(x)
else:
        print("Finally Finished")

#nested loop
adj=["red","big","tast"]
fruits=["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
        

    
