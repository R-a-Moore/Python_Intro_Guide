a = 4
b = 3
print(a+b)
print(a-b)
print(a/b)
print(a%b)
print(a == b)
print(a > b)
print(a <=b)
print(b+b >= a)

# builtin functiosn & methods available in python's library

greeting = "hello world!"
print(greeting.isalpha()) # checks if is boolean value string
if greeting.endswith("!") & greeting.startswith("h"):
    print(greeting, "It's a boy!")

#slicers
print(greeting[-5])
print(greeting[5:])
print(greeting[-4])

#slicers task
print(greeting[6:])
print(greeting[-9])
print(greeting[-8])
print(greeting[-6])

example_string = "james                   james is a James who is a james           "
print(len(example_string)) #get the length
print(len(example_string.strip())) #strips end space characters from text
print(example_string.count("is"))

print(example_string.capitalize()) #capitalizes first character
uppercase_text = "HELLO MY NAME IS CAP I'M A CAPITOL TEXT"
print(uppercase_text.lower()) #makes lower case
print(example_string.replace("james", "son")) # replaces a word in a text with another word

