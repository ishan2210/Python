a="Hello World"
b="Hello,world"

#uppercase
print(a.upper())

#lowercase
print(a.lower())

#strip will remove whitespace from beginning and the end
print(a.strip())

#replace replace with the string
print(a.replace("H","J"))

#The split() method splits the string into substrings if it finds instances of the separator:
print(b.split(","))

#----------------------------------------------------------------------------------------------------------
#String Concatenation

a="Hello"
b="World"
c=a+b
d=a+ " " +b
print(c)
print(d)

#-------------------------------------------------------------------------------------------------------------
#Format String
age=20
txt="My name is ishan and i am {}"
print(txt.format(age))

quantity=7
item=3
price=69
txt="I want item no {}, total quantity of {} at price of rupees {}"
print(txt.format(item,quantity,price))

