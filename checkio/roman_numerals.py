def checkio(data):

    #replace this for solution

    roman_1 = "I"
    roman_5 = "V"
    roman_10 = "X"
    roman_50 = "L"
    roman_100 = "C"
    roman_500 = "D"
    roman_1000 = "M"

    sen = data // 1000
    hyaku = (data - sen * 1000) // 100
    juu = (data - sen*1000 - hyaku * 100) // 10
    ichi = (data - sen*1000 - hyaku * 100 - juu * 10) // 1

    ret = ""

    if sen == 0:
        pass
    elif sen <= 3:
        for i in range(sen):
            ret += roman_1000

    if hyaku == 0:
        pass
    elif hyaku <= 3:
        for i in range(hyaku):
            ret += roman_100
    elif hyaku == 4:
        ret += roman_100 + roman_500
    elif hyaku <= 8:
        ret += roman_500
        for i in range(hyaku-5):
            ret += roman_100
    elif hyaku == 9:
        ret += roman_100 + roman_1000


    if juu == 0:
        pass
    elif juu <= 3:
        for i in range(juu):
            ret += roman_10
    elif juu == 4:
        ret += roman_10 + roman_50
    elif juu <= 8:
        ret += roman_50
        for i in range(juu-5):
            ret += roman_10
    elif juu == 9:
        ret += roman_10 + roman_100

    if ichi == 0:
        pass
    elif ichi <= 3:
        for i in range(ichi):
            ret += roman_1
    elif ichi == 4:
        ret += roman_1 + roman_5
    elif ichi <= 8:
        ret += roman_5
        for i in range(ichi-5):
            ret += roman_1
    elif ichi == 9:
        ret += roman_1 + roman_10

    return ret


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(6))# == 'VI', '6'
    print(checkio(76))# == 'LXXVI', '76'
    print(checkio(499))# == 'CDXCIX', '499'
    print(checkio(3888))# == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')