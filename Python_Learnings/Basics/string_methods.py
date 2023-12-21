#replace() ,strip(),lower(),casefold(),center(),count(),encode(),expandtabs(),upper(),capitalize(),isdigit(),isalpha(),startswith(),endswith(),find()
# format(),format_map()
"""
****
String Methods:
****
Methods which will be useful to create or modify or replace the certain part in the string

-------Built in string methods------------
len()--->to find the length of a string.

find()-->returns the index of a character or a part of the first occurance of a string.

capitalize()--->Converts the first character of a string in to upper cases.

lower()--->converts all the characters in to lower cases.

upper()--->converts all the characters in to upper case.

center()-->This method is useful to align the string to the center using a specified character, SPace is the default character.

expandtabs()-->The expandtabs() method sets the tabsize to the specified no of whitespaces.

format()-->Used to format the strings. Bysing the curley Brackets{} we can achieve this.
    The Placeholders can be identified using the named indexes {prices}, numbered indexes{0}, or even empty brackets {}

startswith()-->returns true if the part of the string is started with the mentioned characters.

endswith()-->returns true if the string ends with the mentioned part of the string.

replace()-->Used to replace the part of the string or the word with the other part of the text or characeter.

casefold()--->It is as same as the lower() method [Converts the characters in to lower case].

isdigit()--->If the entered string has all the digits then it returns True.

strip()-->Used to remove the space from the start and the end of the string.

encode()-->Used to encode the part of string in to the required format.

isalpha()-->returns True if the string has all the characters with out any special characters in the string.
"""

#len() Function
name="m\ta\th\te\ts\th"
print("Length of the string :",len(name))

#find()
print("using the find() method :",name.find("h"))

#captalize()
print("capitalize() :",name.capitalize())

#lower()
print("lower() :",name.lower())

# upper()
print("upper() :",name.upper())

# center(Noof characters,"Special character")
print("center() :",name.center(10,"#"))

# expandtabs(tabsize)
print("expandtabs() :",name.expandtabs(3))

# format()
text="My Name is {name}. Im going to {country} in the month of  {month}"
text.format(name="P Mahesh Kumar",country="Germany",month="August")
print(text.format(name="P Mahesh Kumar",country="Germany",month="August"))
# startswith()
print("startswith() :",name.startswith("aM"))

# endswith()
print("endswith() :",name.endswith("ah"))

#replace()
print("replace() :",name.replace("ah","eyu"))

# casefold()
print("casefold() :",name.casefold())

# isdigit()
print("isdigit() :",name.isdigit())

# strip()
print("strip() :",name.strip())

#isalpha()
print("isalpha() :",name.isalpha())

# encode()
txt = "My name is Ståle"
# print(txt.encode(encoding="ascii",errors="strict"))#strict method will raise an error if the character is not able to encode
print(txt.encode(encoding="ascii",errors="backslashreplace"))#replaces the character is not encoded with the backslash [//]
print(txt.encode(encoding="ascii",errors="ignore"))#Ignores the character which is unable to encode
print(txt.encode(encoding="ascii",errors="namereplace"))#Replaces the character with the text explaining the character
print(txt.encode(encoding="ascii",errors="replace"))#Replaces the character with the question mark which is not able to encode
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))#Replaces the character with the xml character


