class Node:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def print_ll(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} -->",end=" ")
                n = n.next 

def array_to_linkedlist(arr):
    ll = LinkedList()
    for i in reversed(arr):
        ll.add_begin(i)
    return ll

new_arr = [8,7,6,5,4,3,2]

new_ll = array_to_linkedlist(new_arr)
new_ll.print_ll()

