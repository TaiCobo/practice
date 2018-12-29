def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return 0

    even_element_sum = 0
    for i, j in enumerate(array):
        if i % 2 == 0:
            even_element_sum += j

    return even_element_sum * array[-1]


# def checkio(array):
#     return sum(array[i]*array[-1] for i in range(0,len(array),2))


# def checkio(array):
#     return sum(num for i, num in enumerate(array) if not i % 2) * array[-1] if array else 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([0, 1, 2, 3, 4, 5]))
    print(checkio([1, 3, 5]))
    print(checkio([6]))
    print(checkio([]))# == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

