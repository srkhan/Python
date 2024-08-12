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

#Divison is decimal by default
print(5/2)

#Double slash rounds down
print(5//2)

#CAREFUL: most languages round towards 0 by
# default so negative numbers will round down
#adding new commits
#second commit
#3rd commit
#4th commit
print(-3 // 2)