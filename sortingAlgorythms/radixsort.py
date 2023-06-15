class RadixSort:
    @staticmethod
    def radix_sort(array):
        def count_sort(array, exp):
            n = len(array)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = (array[i] // exp) % 10
                count[index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = (array[i] // exp) % 10
                output[count[index] - 1] = array[i]
                count[index] -= 1
                i -= 1

            for i in range(n):
                array[i] = output[i]

        if len(array) == 0:
            return array

        max_value = max(array)
        exp = 1

        while max_value // exp > 0:
            count_sort(array, exp)
            exp *= 10

        return array
