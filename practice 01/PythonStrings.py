print("Hello")
print('Hello')

#slicing strings
b = "Hello, World!"
print(b[2:5])

#modify strings
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']

#concatenate strings
a = "Hello"
b = "World"
c = a + b #or c = a + " " + b
print(c)

#format strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#escape characters
txt = "We are the so-called \"Vikings\" from the north."

#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value	
