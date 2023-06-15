class QuickSort:

    @staticmethod
    def partition(array, p, r):
        pivot = array[r]
        smaller = p

        for x in range(p, r):
            if array[x] <= pivot:
                (array[x], array[smaller]) = (array[smaller], array[x])
                smaller += 1

        (array[smaller], array[r]) = (array[r], array[smaller])

        return smaller

    @staticmethod
    def quicksort(array, p, r):
        if p < r:
            q = QuickSort.partition(array, p, r)
            QuickSort.quicksort(array, p, q - 1)
            QuickSort.quicksort(array, q + 1, r)
