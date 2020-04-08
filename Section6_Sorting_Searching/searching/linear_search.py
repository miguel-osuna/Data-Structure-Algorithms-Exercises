def unordered_linear_search(numlist, num):
    """ Linear Search function for Unordered Lists """
    found = False
    pos = 0
    while pos < len(numlist) and not found:
        if numlist[pos] == num:
            found = True
        else:
            pos = pos + 1
    return found


def ordered_linear_search(numlist, num):
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


def main():
    numlist = [2, 4, 6, 8, 10]
    print(unordered_linear_search(numlist, 2))
    print(unordered_linear_search(numlist, 1))
    print(ordered_linear_search(numlist, 2))
    print(ordered_linear_search(numlist, 5))


if __name__ == "__main__":
    main()
