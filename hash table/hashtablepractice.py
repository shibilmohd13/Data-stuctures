from multiprocessing import cpu_count


class Node:
    def __init__(self, key, value) -> None:
        self.value = value
        self.next = None
        self.key = key

class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            new_node = Node(key, value)
            self.table[index] = new_node
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                print(current.value)
                return
            current = current.next
        raise KeyError("Key not found")

    def remove(self, key):
        index = self._hash(key)

        current = self.table[index]
        previous = None

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError("key not found")
