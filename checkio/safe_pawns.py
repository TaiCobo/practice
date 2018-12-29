def safe_pawns(pawns: set) -> int:

    from string import ascii_lowercase
    word = ascii_lowercase
    ret = 0
    for zahyo in pawns:
        x = zahyo[0:1]
        y = zahyo[1:2]

        for iii in pawns:
            if x == "a":
                left = ""
            else:
                left = ascii_lowercase[ascii_lowercase.index(x)-1] + str(int(y) -1)

            right = ascii_lowercase[ascii_lowercase.index(x)+1] + str(int(y) -1)
            print(left + ":" + right)
            if iii == left or iii == right:
                ret += 1
                break
    return ret


# def safe_pawns(data):
#     return len([1 for i in data if [int(i[1]) - 1, ord(i[0]) + 1] in [[int(k[1]), ord(k[0])] for k in data]
#                 or [int(i[1]) - 1, ord(i[0]) - 1] in [[int(k[1]), ord(k[0])] for k in data]])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))# == 6
    print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))# == 1
    print(safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"]))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")