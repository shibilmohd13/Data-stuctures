class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue elements:")
queue.display()

print("Dequeue:", queue.dequeue())
print("Queue elements after dequeue:")
queue.display()

print("Front of the queue:", queue.peek())
