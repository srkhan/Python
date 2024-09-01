# python interview prep
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

# Divison is decimal by default in python
print(5/2)

# Double slash rounds down
print(5//2)

# CAREFUL: most languages round towards 0 by
# default so negative numbers will round down
print(-3 // 2)
 
# a workaround for rounding towards zero is to
# use decimal divison and then convert to int.
print (int(-3/2))

# modding similar to most languages
print (10%3)

# except for negative values
print (-10%3)

# to be consistent with other languages modulo
import math
print(math.fmod(-10,3))

# more math helpers
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

# max / min int
float ("inf")
float ("-inf")

# python numbers are infinite so they never overflow
print(math.pow(2, 200))

# but still less than infinity
print(math.pow(2, 200) < float("inf"))

# arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

# can be used as a stack 
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

# can insert into the middle, eg. inseretd 7 at index 1 of arr
arr.insert(1,7)
print(arr)

# unlike pusing and popping from array inserting into the middle
# of an array is BIG O of n time operation

# indexing an array is not a BIG O of n time operation 
# so at index 0 and index 3 we can read the values and reassign values
# these operations above are constant time operations
arr[0] = 0
arr[3] = 0
print (arr)

#To Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful: -1 is not out of bounds,
# it's the last value
arr = [1, 2, 3]
print(arr[-1])

# Indexing -2 is hte second to last value, etc.
print(arr[-2])

# Sublists (aka slicing an array)

arr = [1, 2, 3, 4]
# doesnt include last index
print(arr[1:3])

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# becareful vars on the left side match # of elements in array 
#a, b = [2, 4, 5]

# loop through arrays
nums = [1, 2, 3]

# using index
for i in range(len(nums)):
    print(nums[i])

# without index
for n in nums:
    print(n)

# with index and value
for i, n in enumerate(nums):
    print("enumerate ", i, n)

# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)

# Sorting, sorts in ascending order by default
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

# sort is done by alphabetical order on a list of strings
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

# Custom sort (by length of string)
# key is equal to lambda (function w/o name)
# take every single value from arr, call it x
# return the length of x, and use that as the key to
# use to sort the arr
arr.sort(key=lambda x: len(x))
print(arr)

# List comprehension
arr = [i for i in range(5)]
print(arr)

arr = [i+i for i in range(5)]
print(arr)

# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)

# This won't work, each of the 4 rows of the arry will be the same, modifying one row will modify all rows
arr = [[0]* 4] * 4
print(arr)

# Strings are similar to arrays
s = "abc"
print(s[0:2])

# But they are immutable, cant reassign the character at index 0
#s[0] = "A"

# So this cerates a new string, addingd def to the end of the string
# creates a new string, modifying a string is considered n time operation
s += "def"
print(s)

# Valid numeric strings can be converted
# strings can be converted to integers and the integers can be added
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# In rare cases you may need the ASCII value of a char
print(ord("a"))
print(ord("b"))

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))

#Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

# popleft operation is constant time unlike stacks
queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)

# HashSet
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

# list to set
print(set([1, 2, 3]))

# Set comprehension
mySet = { i for i in range(5)}
print(mySet)

# HashMap (aka dict (dictionaries))
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

# modify value that is mapped to a key
myMap["alice"] = 80
print(myMap["alice"])

# search if a key exists in a hashmap at constant time
print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

# initalize hashmap
myMap = { "alice": 90, "bob": 70 }
print(myMap)

# Dict comprehension
myMap = { i: 2*i for i in range(3)}
print(myMap)

# Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])

# directly iterate through the values of hashmap if no key is needed 
for val in myMap.values():
    print(val)

# using unpacking, go through items of the map, that will give us keys and values
for key, val in myMap.items():
    print(key, val)

# Tuples are like arrrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# Can't modify
#tup[0] = 0

# Can be used as key for has map/set
myMap = { (1,2): 3 }
print(myMap[(1,2)])

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

# Lists can't be keys
# myMap[[3,4]] = 5

# Heaps
import heapq

# under the hood heaps are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 10)

# min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# No max heaps by default, work around is to use
# min heap and multiply by -1 when push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap, -10)

# max is always at index 0
print(-1 * maxHeap[0])

# multiplying by -1 when pushing and then agian for popping negates it and prints out in 
# greatest to smallest
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

# Functions
def myFunc(n, m):
    return n * m

print(myFunc(3, 4))

# Nested functions have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))

# Can modify objects but not reassign unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 6
double(nums, val)

# Class
class MyClass:
    # Constructor
    def __init__(self, nums): 
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()
nums = [1, 2, 3, 4]
# TODO figure out why Line 428 gives "AttributeError: 'list' object has no attribute 'size'" error
#print(MyClass.getLength(nums))



