# def popular_words(text: str, words: list) -> dict:
#     # your code here
#
#     list = []
#     for string in text.replace("\n", " ").split(" "):
#         list.append(str(string).lower())
#
#     print(list.count("i"))
#
#     ret = {}
#     for word in words:
#         ret[word] = list.count(word)
#
#     return ret
#
#

def popular_words(text: str, words: list) -> dict:
    # your code here
    return {word: text.lower().split().count(word) for word in words}

# popular_words=lambda t,w:{l:t.lower().split().count(l)for l in w}

if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    })
    print("Coding complete? Click 'Check' to earn cool rewards!")