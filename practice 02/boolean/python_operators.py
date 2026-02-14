print(10 + 5)
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

#Arithmetic Operators
#+	Addition ---> x + y	
#-	Subtraction	---> x - y	
#*	Multiplication	---> x * y	
#/	Division ---> x / y	
#%	Modulus	---> x % y	
#**	Exponentiation	---> x ** y	
#//	Floor division	---> x // y
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Assignment Operators
#=	---> x = 5	---> x = 5	
#+=	---> x += 3	---> x = x + 3	
#-=	---> x -= 3	---> x = x - 3	
#*=	---> x *= 3	---> x = x * 3	
#/=	---> x /= 3	---> x = x / 3	
#%=	---> x %= 3	---> x = x % 3	
#//= ---> x //= 3 ---> x = x // 3	
#**= ---> x **= 3 ---> x = x ** 3	
#&=	---> x &= 3	---> x = x & 3	
#|=	---> x |= 3	---> x = x | 3	
#^=	---> x ^= 3	---> x = x ^ 3	
#>>= ---> x >>= 3 ---> x = x >> 3	
#<<= ---> x <<= 3 ---> x = x << 3	
#:=	---> print(x := 3) ---> x = 3 print(x)
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Comparison Operators
#==	Equal ---> x == y	
#!=	Not equal ---> x != y	
#>	Greater than ---> x > y	
#<	Less than ---> x < y	
#>=	Greater than or equal to ---> x >= y	
#<=	Less than or equal to ---> x <= y	
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical Operators
#and 	Returns True if both statements are true ---> x < 5 and  x < 10	
#or	Returns True if one of the statements is true ---> x < 5 or x < 4	
#not	Reverse the result, returns False if the result is true	---> not(x < 5 and x < 10)
x = 5

print(x > 0 and x < 10)
x = 5

print(not(x > 3 and x < 10))

#Identity Operators
#is 	Returns True if both variables are the same object	---> x is y	
#is not	Returns True if both variables are not the same object	---> x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#Membership Operators
#in 	Returns True if a sequence with the specified value is present in the object	---> x in y	
#not in	Returns True if a sequence with the specified value is not present in the object	---> x not in y	
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
