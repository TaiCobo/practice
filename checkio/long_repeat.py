def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    max_len = 0
    this_len = 1
    if len(line) <= 1:
        return len(line)

    for i in range(0, len(line)-1):
        if line[i:i+1] == line[i+1:i+2]:
            this_len += 1
        else:
            if max_len < this_len:
                max_len = this_len
            this_len = 1

    if max_len < this_len:
        max_len = this_len

    return max_len


# def long_repeat(line):
#     import re
#     max_symbols = 0
#     for symbol in list(set(line)):
#         max_symbol_in_line = len(max(re.findall('{}+'.format(symbol), line)))
#         if max_symbol_in_line > max_symbols:
#             max_symbols = max_symbol_in_line
#     return max_symbols


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(long_repeat('sdsffffse'))# == 4, "First"
    print(long_repeat('ddvvrwwwrggg'))# == 3, "Second"
    print(long_repeat('abababaab'))# == 2, "Third"
    print(long_repeat(''))# == 0, "Empty"
    print(long_repeat('aa'))# == 0, "Empty"
    print('"Run" is good. How is "Check"?')