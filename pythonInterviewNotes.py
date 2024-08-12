#python interview prep
hi = "Hi this is sadad"
hello = "bruh"
print(hi)
print(hello)

# Multiple assignments
n, m = 0, "abc"
n, m, z = 0.125, "abc", False
print("n =", n)
print("z =", z)

# Increment 
n = n + 1 # good
n += 1 # good
# n++ # bad

# None is null (absence of value)
n = 4
n = None
print("n =", n)

# If statements don't need parentheses
# or curly braces
n = 1
if n > 2:  
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parenthesis needed for multiline conditionals
# and = && s
# or = ||
n, m = 1, 2
if ((n > 2 and
    n != m) or n == m):
    n += 1

# While loops are similar  
n = 0
while n < 5:
    print(n)
    n += 1

# Looping from i = 0 to i = 4
for i in range(5):
    print(i)
for i in range(2, 6):
    print(i)
for i in range(5, 1, -1):
    print(i)    

#Divison is decimal by default in python
print(5/2)

#Double slash rounds down
print(5//2)

#CAREFUL: most languages round towards 0 by
# default so negative numbers will round down
print(-3 // 2)
 
# a workaround for rounding towards zero is to
#use decimal divison and then convert to int.
print (int(-3/2))

#modding similar to most languages
print (10%3)

#except for negative values
print (-10%3)

#to be consistent with other languages modulo
import math
print(math.fmod(-10,3))

#more math helpers
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

#max / min int
float ("inf")
float ("-inf")

#python numbers are infinite so they never overflow
print(math.pow(2, 200))

#but still less than infinity
print(math.pow(2, 200) < float("inf"))

#arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

