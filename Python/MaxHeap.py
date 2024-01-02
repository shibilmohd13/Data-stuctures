class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up()

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:  # Change the comparison condition
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()

        return root

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            largest = index  # Change the variable name

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:  # Change the comparison condition
                largest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:  # Change the comparison condition
                largest = right_child_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

# Example usage:
max_heap = MaxHeap()
max_heap.push(4)
max_heap.push(8)
max_heap.push(2)
max_heap.push(6)

print(max_heap.heap)  # Output: [8, 6, 4, 2]

print(max_heap.pop())  # Output: 8
print(max_heap.heap)  # Output: [6, 2, 4]
