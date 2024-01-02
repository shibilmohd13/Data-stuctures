class Stack:
    
    def __init__(self) -> None:
        self.items = []

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



# Example usage
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)  # Output: [1, 2, 3]

print("Top element:", stack.peek())  # Output: 3

popped_element = stack.pop()
print("Popped element:", popped_element)  # Output: 3

print("Stack size:", stack.size())  # Output: 2
