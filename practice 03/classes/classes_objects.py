#CREATE A CLASS
class MyClass:
    x = 5

#CREATE OBJECT
p1 = MyClass()
print(p1.x)

#DELETE OBJECT
del p1

#MULTIPLE OBJECT
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#PASS STATEMENT
class Person:
    pass