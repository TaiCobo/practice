def checkio(words: str) -> bool:

    # ret = False
    #
    # for word in words.split():
    #     if word.isnumeric():
    #         continue
    #     elif word.isalpha() and len(word) < 3:
    #         ret = False
    #         break
    #     else:
    #         ret = True
    # return ret

    ret = False
    word_list = words.split()
    for i in range(0, len(word_list)-2):
        if word_list[i].isalpha() and word_list[i+1].isalpha() and word_list[i+2].isalpha():
            ret = True
            break
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("Hello World hello"))# == True, "Hello"
    print(checkio("He is 123 man"))# == False, "123 man"
    print(checkio("1 2 3 4"))# == False, "Digits"
    print(checkio("bla bla bla bla"))# == True, "Bla Bla"
    print(checkio("Hi"))# == False, "Hi"

    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
    print(checkio("one two 3 four five 6 seven eight 9 ten eleven 12"))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

