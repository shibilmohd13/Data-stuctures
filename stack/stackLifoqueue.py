from queue import LifoQueue

class Stack:
    def __init__(self) -> None:
        self.items = LifoQueue(maxsize=0)

    def is_empty(self):
        return self.items.empty()

    def is_full(self):
        return self.items.full()

    def size(self):
        return self.items.qsize()
    
    def push(self, data):
        self.items.put(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Empty")
        else:
            return self.items.get()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stck empty")
        else:
            item = self.item.get()
            self.items.put(item)
            return item


        