from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    before_el = ""
    for el in elements:
        if before_el == "":
            before_el = el
        if before_el != el:
            return False
    return True

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    print(all_the_same([1, 1, 1]))# == True
    print(all_the_same([1, 2, 1]))# == False
    print(all_the_same(['a', 'a', 'a']))# == True
    print(all_the_same([]))# == True
    print(all_the_same([1]))# == True
    print("Coding complete? Click 'Check' to earn cool rewards!")