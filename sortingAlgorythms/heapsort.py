class HeapSort:
    @staticmethod
    def max_heapify(array, i, heap_size):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child <= heap_size and array[left_child] > array[largest]:
            largest = left_child

        if right_child <= heap_size and array[right_child] > array[largest]:
            largest = right_child

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            HeapSort.max_heapify(array, largest, heap_size)

        return array

    @staticmethod
    def build_max_heap(array):
        heap_size = len(array) - 1

        for i in range(heap_size // 2, -1, -1):
            HeapSort.max_heapify(array, i, heap_size)

        return array

    @staticmethod
    def heapsort(array):
        heap_size = len(array) - 1
        HeapSort.build_max_heap(array)

        for i in range(heap_size, 0, -1):
            array[i], array[0] = array[0], array[i]
            heap_size -= 1
            HeapSort.max_heapify(array, 0, heap_size)

        return array
