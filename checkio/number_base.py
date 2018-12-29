def checkio(str_number: str, radix: int) -> int:

    try:
        return int(str_number, radix)
    except:
        return -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("AF", 16))# == 175, "Hex"
    print(checkio("101", 2))# == 5, "Bin"
    print(checkio("101", 5))# == 26, "5 base"
    print(checkio("Z", 36))# == 35, "Z base"
    print(checkio("AB", 10))# == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

