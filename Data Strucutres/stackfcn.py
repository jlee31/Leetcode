class Empty(Exception):

    pass

 

class Stack:

    def __init__(self):

        self.data = []

 

    def __len__(self):

        return len(self.data)

   

    def is_empty(self):

        return len(self.data) == 0

 

    def push(self, value):

        self.data.append(value)

 

    def top(self):

        if self.is_empty():

            raise Empty('Stack is empty')

        return self.data[-1]

       

    def pop(self):

        if self.is_empty():

            raise Empty('Stack is empty')

        return self.data.pop()

   

s = Stack()

s.push(3)

s.push(5)

print(len(s))     # prints: 2

s.pop()

s.pop()

 

try:

    print(s.top())

except Empty as e:

    print(e)       # prints: Stack is empty

def reverse_file(filename):

    S = Stack()

    original = open(filename)

    for line in original:

        S.push(line.rstrip('\n'))

    original.close

 

    output = open(filename, 'w')

    while not S.is_empty():

        output.write(S.pop() + '\n')

    output.close()

 

reverse_file('test.txt')

def isMatched(expression):
    left = '([{' 
    right = ')]}' 
    s = Stack() 
    for c in expression: 
        if c in left: s.push(c) 
        elif c in right: 
            if s.is_empty(): return False 
            
            if right.index(c) != left.index(s.pop()): return False
            
    return s.is_empty()