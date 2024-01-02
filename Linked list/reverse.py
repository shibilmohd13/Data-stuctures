
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
                print(f"{n.data} --> ",end=" ")
                n = n.next
    
    def reverse(self, head):
        new_list = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        
        return new_list


ll1 = LinkedList()
ll1.head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
ll1.print_ll()
ll_rev = LinkedList()
ll_rev.head = ll1.reverse(ll1.head)
ll_rev.print_ll()

