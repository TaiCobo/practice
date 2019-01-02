
def checkio(n, m):

    summary = str(int(format(n, 'b')) + int(format(m, 'b')))
    cnt = 0
    for i in range(len(summary)):
        if summary[i:i+1] == "1":
            cnt += 1
    return cnt


# def checkio(n, m):
#     return bin(n^m).count('1')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(117, 17))# == 3, "First example"
    print(checkio(1, 2))# == 2, "Second example"
    print(checkio(16, 15))# == 5, "Third example"




