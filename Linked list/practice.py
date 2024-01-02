class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} --> ", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node not found in LinkedList")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
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

    def insert_empty(self, data):
        if self.head is not None:
            print("List is not Empty")
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_value(self, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Element not found")
        else:
            n.ref = n.ref.ref


ll1 = LinkedList()
ll1.add_begin(20)
ll1.add_begin(10)
ll1.add_before(100, 10)
ll1.print_ll()


