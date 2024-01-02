from queue import Queue

class MyQueue:
    def __init__(self):
        self.queue = Queue()

    def is_empty(self):
        return self.queue.empty()

    def enqueue(self, item):
        self.queue.put(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.get()
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        if not self.is_empty():
            # Peek at the front element without removing it
            front_element = self.queue.queue[0]
            return front_element
        else:
            raise IndexError("front from an empty queue")

    def size(self):
        return self.queue.qsize()