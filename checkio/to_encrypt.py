def to_encrypt(text, delta):
    #replace this for solution

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ret = ""

    for word in range(len(text)):
        if text[word] == " ":
            ret += " "
        else:
            ret += alphabet[(alphabet.index(text[word]) + delta) % 26]
    return ret

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(to_encrypt("a b c", 3))# == "d e f"
    print(to_encrypt("a b c", -3))# == "x y z"
    print(to_encrypt("simple text", 16))# == "iycfbu junj"
    print(to_encrypt("important text", 10))# == "swzybdkxd dohd"
    print(to_encrypt("state secret", -13))# == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")