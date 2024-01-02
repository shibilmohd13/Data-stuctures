class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next 
        self.prev = prev
    
class DoublyLL:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} -->",end="")
                n = n.next

    # def 










    

doubly = DoublyLL()
        