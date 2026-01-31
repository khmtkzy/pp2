a = 33
b = 200
if b > a:
    print("b is greater than a")

number = 15
if number > 0:
    print("The number is positive")

age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

is_logged_in = True
if is_logged_in:
    print("Welcome back!")

a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)