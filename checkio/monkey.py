def count_words(text: str, words: set) -> int:

    cnt = 0
    for word in words:
        if text.lower().find(word) != -1:
            cnt += 1
    return cnt

# def count_words(text: str, words: set) -> int:
#     return sum([1 for word in words if word in text.lower()])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))# == 3, "Example"
    print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))# == 2, "BANANAS!"
    print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}))# == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")