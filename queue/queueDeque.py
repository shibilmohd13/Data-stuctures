from collections import deque

class Queue:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty() :
            raise IndexError("Stack empty")
        else:
            return self.items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("Stack empty")
        else:
            return self.items[0]