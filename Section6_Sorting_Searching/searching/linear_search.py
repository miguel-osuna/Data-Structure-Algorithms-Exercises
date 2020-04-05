def unorderedLinearSearch(numlist, num):
    """ Linear Search function for Unordered Lists """
    found = False
    pos = 0
    while pos < len(numlist) and not found:
        if numlist[pos] == num:
            found = True
        else:
            pos = pos + 1
    return found


def orderedLinearSearch(numlist, num):
    """ Linear Search function for Ordered Lists """
    found = False
    stop = False
    pos = 0
    while pos < len(numlist) and not found and not stop:
        if numlist[pos] == num:
            found = True
        else:
            if numlist[pos] > num:
                stop = True
            else:
                pos = pos + 1
    return found


if __name__ == "__main__":
    numlist = [2, 4, 6, 8, 10]
    print(unorderedLinearSearch(numlist, 2))
    print(unorderedLinearSearch(numlist, 1))
    print(orderedLinearSearch(numlist, 2))
    print(orderedLinearSearch(numlist, 5))
