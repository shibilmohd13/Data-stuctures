class Maxheap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up()

    def heapify_up(self):
        index = len(self.heap) - 1

        while index > 0:
            parent_index = (len(self.heap) - 1) // 2

            if self.heap[index] > self.heap[parent_index]:
                self.heap[index] , self.heap[parent_index] = self.heap[parent_index],  self.heap[index]
                index = parent_index
            else:
                break

    def pop(self):

        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()

        return node

    def heapify_down(self):
        index = 0

        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            largest = index

            if left_child_index < len(self.heap) and self.heap[largest] < self.heap[left_child_index]:
                largest = left_child_index
            
            if right_child_index < len(self.heap) and self.heap[largest] < self.heap[right_child_index]:
                largest = right_child_index

            if largest != index:
                self.heap[largest] , self.heap[index] = self.heap[index] , self.heap[largest]
                index = largest
            else:
                break


# Example usage:
max_heap = Maxheap()
max_heap.insert(4)
max_heap.insert(8)
max_heap.insert(2)
max_heap.insert(6)

print(max_heap.heap)  # Output: [8, 6, 4, 2]

print(max_heap.pop())  # Output: 8
print(max_heap.heap)  # Output: [6, 2, 4]

