
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
                print(n.data)
                n = n.next

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(f"Middle is :- {slow.data}")

ll1 = LinkedList()
ll1.head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
ll1.find_middle()

ll1.print_ll()
