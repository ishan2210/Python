thisdict= {
    "brand": "Ford",
    "Model": "Mustang",
    "Year": 1969
}
print(thisdict)

thisdict= {
    "brand": "Samsung",
    "Model": "S23",
    "Price": "70000"

}
print(thisdict)

#Print the "brand" value of the dictionary:
thisdict= {

    "Brand": "BMW",
    "Model": "X7",
    "Year":  "2022",
    "Price": "1CR"
}
print(thisdict["Brand"])

#Dictionaries cannot have two items with the same key:
#Duplicate values will overwrite existing values:
thisdict2= {
    "Brand": "Boat",
    "Model": "Airdopes 441",
    "year": "1970",
    "year": "1971"
}
print(thisdict2)
print(len(thisdict2))

thisdict3= {
    "brand": "ford",
    "model": "Endeavour",
    "year": "2020"
}
print(type(thisdict3))

#It is also possible to use the dict() constructor to make a dictionary.
thisdict4= dict(name= "ishan", country= "australia",age=20)
print(thisdict4)

