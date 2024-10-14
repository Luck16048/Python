class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def remove_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def build_heap(self, array):
        self.heap = array
        for i in range(len(array) // 2, -1, -1):
            self._heapify_down(i)

def main():
    heap = MaxHeap()
    heap.build_heap([3, 1, 4, 1, 5, 9, 2, 6])
    print("Elementy kopca:", heap.heap)
    print("Usunięty największy element:", heap.remove_max())
    print("Elementy kopca po usunięciu:", heap.heap)

if __name__ == "__main__":
    main()
