
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} -->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.add_begin(data)
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            if n is None:
                print("Element not found")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
        
    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.data == x:
            new_node = Node(data) #  --\
            new_node.ref = self.head #   >  Add at begin 
            self.head = new_node #   --/
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Element not found")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_value(self, x):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.data == x:
                self.head = self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("value not found")
            else:
                n.ref = n.ref.ref
        


obj = LinkedList()
obj.add_begin(10)
obj.add_begin(20)
obj.add_end(30)
obj.add_after(50, 10)
obj.add_before(80, 50)
obj.delete_begin()
obj.delete_end()
obj.delete_value(80)



obj.print_ll()
