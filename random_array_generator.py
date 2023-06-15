import numpy


class ArrayOperator:

    @staticmethod
    def generateMeRandomArray(length):
        return numpy.random.randint(1, 1_000_000, length)
