from queue import PriorityQueue

class Queue:

    def __init__(self) -> None:
        self.items = PriorityQueue()

    def is_empty(self):
        return self.items.empty()

    def enqueue(self, data, priority):
        self.items.put((priority, data))
    
    def dequeue(self):
        if self.items.empty():
            print("Empty")

        else:
            return self.items.get()[1]


priority_queue_queue = Queue()

priority_queue_queue.enqueue("Task A", 3)
priority_queue_queue.enqueue("Task B", 1)
priority_queue_queue.enqueue("Task C", 2)

print(priority_queue_queue)

while not priority_queue_queue.is_empty():
    task = priority_queue_queue.dequeue()
    print(f"Dequeued Task: {task}")
        
