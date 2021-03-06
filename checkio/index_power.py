def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
    """

    if n + 1 > len(array):
        return -1
    else:
        return array[n] ** n

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(index_power([1, 2, 3, 4], 2))# == 9, "Square"
    print(index_power([1, 3, 10, 100], 3))# == 1000000, "Cube"
    print(index_power([0, 1], 0))# == 1, "Zero power"
    print(index_power([1, 2], 3))# == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")