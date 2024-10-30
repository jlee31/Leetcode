# Python Syntax for Leetcode

# Variables
name = "Joseph"
num = 1
lst = [1,2,3]

# Classes
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

node = ListNode(1)

print(node.val) # 1
print(node.next) # none

# Loops
arr = [1,2,3,4]
for i in range(len(arr)):
    print(arr[i])

index = len(arr)
while index >= 0:
    print(index)
    index -= 1

# Bool
result = True or False
result = True and (False and False)
hi = 1 == 1
bye = 1 != 2

# Max / Min Operator
result = max(5,2)
result = min(5,2)
print(result)

# Dictionaries
dictionary = {}
{
    "key": "value"
}

dictionary[10] = "code"
dictionary["A"] = 10
print(dictionary)

if "A" in dictionary:
    print(True)
else:
    print(False)

# Strings
str = "AB CD E"
splitStr = str.split(" ")
print(splitStr)

resultString =  "".join(splitStr)
print(resultString)

str = "Joseph"
strArr = list(str)
print(strArr)
strArr[0], strArr[1] = strArr[1], strArr[0]
print(strArr)
result2string = "".join(strArr)
print(result2string)


