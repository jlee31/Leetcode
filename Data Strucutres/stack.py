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