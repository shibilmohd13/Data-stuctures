from collections import deque
from inspect import stack

class Stack:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty() :
            raise IndexError("Stack empty")
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack empty")
        else:
            return self.items[-1]

    def rev(self):
        return self.items.reverse()

    
obj = Stack()

obj.push(1)
obj.push(2)
obj.push(3)

obj.rev()

print(obj.peek())

