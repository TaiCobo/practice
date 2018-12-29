# def best_stock(data):
#     # your code here
#     maxval = -1.00
#     maxkey = ""
#     for key in data:
#         if data[key] > maxval:
#             maxval = data[key]
#             maxkey = key
#     return maxkey



def best_stock(data):
    return max(data, key=lambda x: data[x])

# def best_stock(data):
#     return max(data.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))# == 'ATX', "First"
    print(best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }))# == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")

