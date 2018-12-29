def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """

    import collections
    c = collections.Counter(data)
    return c.most_common(1)[0][0]


    # return max(data,key=data.count)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))# == 'a'

    print(most_frequent(['a', 'a', 'bi', 'bi', 'bi']))# == 'bi'
    print('Done')