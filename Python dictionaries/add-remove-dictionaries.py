#add items
thisdict= {
    "name": "ishan",
    "age": 20,
    "country": "india"
}
thisdict["color"]="brown"
print(thisdict)

thisdict= {
    "name": "ishan",
    "country": "india"
}
thisdict.update({"year": 20})

#remove items
thisdict1= {
    "name": "ishan",
    "age": 20,
    "country": "india"
}
thisdict1.pop("age")
print(thisdict1)

thisdict2={
    "name": "ishan",
    "country": "india",
    "age": 20
}
thisdict2.popitem()
print(thisdict2)

thisdict3={
    "name": "ishan",
    "country": "india",
    "age": 20
}
del thisdict3["name"]
print(thisdict3)

thisdict4={
    "name": "ishan",
    "age": 20,
    "country": "india"
}
thisdict4.clear()
print(thisdict4)

#copydictionary
thisdict5={
    "name": "ishan",
    "country": "india",
    "age": 20
}
mydict=thisdict5.copy()
print(mydict)

thisdict6={
    "name": "ishan",
    "country": "india",
    "age": 20
}
mydict2=dict(thisdict6)
print(mydict2)
