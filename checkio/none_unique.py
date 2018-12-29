#Your optional code here
#You can import some modules or create additional functions


def checkio(data: list) -> list:

    list = []
    for word in data:
        if data.count(word) >= 2:
            list.append(word)
    return list


# def checkio(data: list) -> list:
#     return [ num for num in data if data.count(num)>1]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(list(checkio([1, 2, 3, 1, 3])))# == [1, 3, 1, 3], "1st example"
    print(list(checkio([1, 2, 3, 4, 5])))# == [], "2nd example"
    print(list(checkio([5, 5, 5, 5, 5])))# == [5, 5, 5, 5, 5], "3rd example"
    print(list(checkio([10, 9, 10, 10, 9, 8])))# == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

