class Minheap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._heapify_up()

    def _heapify_up(self):
        index = len(self.heap) -1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index] , self.heap[parent_index] = self.heap[parent_index] , self.heap[index]
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

            smallest = index

            if left_child_index < len(self.heap) and self.heap[smallest] > self.heap[left_child_index]:
                smallest = left_child_index
            if right_child_index < len(self.heap) and self.heap[smallest] > self.heap[right_child_index]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index] , self.heap[smallest] = self.heap[smallest] ,self.heap[index]
                index = smallest 
            else:
                break