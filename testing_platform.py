import sys
import time

from random_array_generator import ArrayOperator
from sortingAlgorythms.heapsort import HeapSort
from sortingAlgorythms.quicksort import QuickSort
from sortingAlgorythms.radixsort import RadixSort


class AlgorithmsPerformer:

    @staticmethod
    def start_mesurements():
        sys.setrecursionlimit(10 ** 6)
        array_original = ArrayOperator.generateMeRandomArray(8_000)
        array_reversed = list(reversed(array_original.copy()))
        array_sorted = RadixSort.radix_sort(array_original.copy())

        print("Alg1 - Heapsort\n")

        start_time = time.time()
        HeapSort.heapsort(array_original.copy())
        end_time = time.time()

        print(f"Heapsort - original. Execution time: {end_time - start_time} seconds\n")

        start_time = time.time()
        HeapSort.heapsort(array_reversed.copy())
        end_time = time.time()

        print(f"Heapsort - reversed. Execution time: {end_time - start_time} seconds\n")

        start_time = time.time()
        HeapSort.heapsort(array_sorted.copy())
        end_time = time.time()

        print(f"Heapsort - sorted. Execution time: {end_time - start_time} seconds\n\n\n\n")

        print("Alg2 - Quicksort\n")

        start_time = time.time()
        QuickSort.quicksort(array_original.copy(), 0, len(array_original) - 1)
        end_time = time.time()

        print(f"Quicksort - original. Execution time: {end_time - start_time} seconds\n")

        start_time = time.time()
        QuickSort.quicksort(array_reversed.copy(), 0, len(array_reversed) - 1)
        end_time = time.time()

        print(f"Quicksort - reversed. Execution time: {end_time - start_time} seconds\n")

        start_time = time.time()
        QuickSort.quicksort(array_sorted.copy(), 0, len(array_sorted) - 1)
        end_time = time.time()

        print(f"Quicksort - sorted. Execution time: {end_time - start_time} seconds\n\n\n\n")

        print("Alg3 - Radix (LSD) sort\n")

        start_time = time.time()
        RadixSort.radix_sort(array_original.copy())
        end_time = time.time()

        print(f"Radix - original. Execution time: {end_time - start_time} seconds\n")

        start_time = time.time()
        RadixSort.radix_sort(array_reversed.copy())
        end_time = time.time()

        print(f"Radix - reversed. Execution time: {end_time - start_time} seconds\n")

        start_time = time.time()
        RadixSort.radix_sort(array_sorted.copy())
        end_time = time.time()

        print(f"Radix - sorted. Execution time: {end_time - start_time} seconds\n")
