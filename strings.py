a="hello"
print(a)

#multiline Strings
b= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(b)

"""
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
"""
#Get the character at position 1 (remember that the first character has the position 0):
a="Hello world"
print(a[1])

#In string len always start with position 1 also counts spacing
a="Hello world"
print(len(a))

#Check String To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "ishan kansara here"
print("kansara" in txt)

