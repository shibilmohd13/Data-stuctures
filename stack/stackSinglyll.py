class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Stack:

    def __init__(self) -> None:
        self.top = None

    def __str__(self) -> str:
        name = ''
        if self.top is None:
            return 'Empty stck'
        else:
            current = self.top
            while current:
                name += f"{current.val} -> " 
                current = current.next
            return name[:-3]
    
    def is_empty(self):
        return self.top == None

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack empty")
        else: 
            print(self.top.val)
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack empty")
        else:
            self.top = self.top.next

    def size(self):
        if self.top is None:
            print("Empty stack")
        else:
            current = self.top
            count = 0
            while current:
                count += 1
                current = current.next
            print(count)


stack = Stack()

# print(stack.peek())
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.peek()
stack.size()

print(stack)
