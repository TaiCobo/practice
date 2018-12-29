def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """

    ret = ""

    return ",".join(phrases).replace("right", "left")


def checkio(number: int) -> int:

    nnn = str(number)
    ret = 1
    for i, val in enumerate(range(0, len(nnn))):
        if nnn[i] == "0":
            continue
        ret = ret * int(nnn[i])
    return ret


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # print(left_join(("left", "right", "left", "stop")))# == "left,left,left,stop", "All to left"
    # print(left_join(("bright aright", "ok")))# == "bleft aleft,ok", "Bright Left"
    # print(left_join(("brightness wright",)))# == "bleftness wleft", "One phrase"
    # print(left_join(("enough", "jokes")))# == "enough,jokes", "Nothing to replace"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    print(checkio(123405))
    print(checkio(999))# == 729
    print(checkio(1000))# == 1
    print(checkio(1111))# == 1