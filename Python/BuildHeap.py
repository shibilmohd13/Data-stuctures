class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def heapify_array(self, array):
        self.heap = array
        n = len(self.heap)

        # Starting from the last non-leaf node and heapify down
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down_at_index(i)

    def _heapify_down_at_index(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            smallest = index

            if left_child_index < len(self.heap) and self.heap[smallest] > self.heap[left_child_index]:
                smallest = left_child_index
            if right_child_index < len(self.heap) and self.heap[smallest] > self.heap[right_child_index]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

# Example usage:
min_heap = MinHeap()
array_to_heapify = [4, 10, 3, 5, 1]
min_heap.heapify_array(array_to_heapify)
print(min_heap.heap)  # Output: [1, 4, 3, 5, 10]
