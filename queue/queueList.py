from random import randint


class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue empty")
        else:
            return self.items[0]

    def rear(self):
        if self.is_empty():
            raise IndexError("Queue empty")
        else:
            return self.items[1]

    def size(self):
        return len(self.items)
    

