def largest_histogram(histogram):

    max_size = 0
    for i in range(len(histogram)):
        for j in range(i, len(histogram)):
            this_size = (j - i +1) * min(histogram[i:j+1])
            # print("i:" + str(i) + "  j:" + str(j) + "   " + str(this_size) + "    " + str(min(histogram[i:j+1])))

            if max_size < this_size:
                max_size = this_size
    return max_size

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(largest_histogram([5]))# == 5, "one is always the biggest"
    print(largest_histogram([5, 3]))# == 6, "two are smallest X 2"
    print(largest_histogram([1, 1, 4, 1]))# == 4, "vertical"
    print(largest_histogram([1, 1, 3, 1]))# == 4, "horizontal"
    print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))# == 8, "complex"
    print("Done! Go check it!")