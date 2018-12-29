import re
import collections

def checkio(text: str) -> bool:

    list = []
    text_new = text.replace(" ", "")
    for i in range(0, len(text_new)):
        if text_new[i:i+1].isalpha():
            list.append(text_new[i:i+1].upper())
    list.sort()
    c = collections.Counter(list)
    return c.most_common(1)[0][0].lower()


# import re
# from collections import Counter
# def checkio(text: str) -> str:
#     return Counter(sorted("".join(re.findall("[a-z]+", text.lower())))).most_common(1)[0][0]

if __name__ == '__main__':
    print(checkio("Hello World!"))# == "l", "Hello test"
    print(checkio("How do you do?"))# == "o", "O is most wanted"
    print(checkio("One"))# == "e", "All letter only once."
    print(checkio("Oops!"))# == "o", "Don't forget about lower case."
    print(checkio("AAaooo!!!!"))# == "a", "Only letters."
    print(checkio("abe"))# == "a", "The First."
    print("Start the long test")
    print(checkio("a" * 9000 + "b" * 1000))# == "a", "Long."
