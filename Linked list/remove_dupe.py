class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} -->",end=" ")
                n = n.next
    
    def remove_duplicate(self):
        current = self.head
        while current and current.next :
            if current.data == current.next.data:
                current.next = current.next.next 
            current = current.next
        

ll1 = LinkedList()
ll1.head = Node(1, Node(2, Node(2, Node(4, Node(4)))))
ll1.remove_duplicate()
ll1.print_ll()
