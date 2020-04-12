def unordered_linear_search(num_list, num):
    """ Linear Search function for Unordered Lists """
    found = False
    pos = 0
    while pos < len(num_list) and not found:
        if num_list[pos] == num:
            found = True
        else:
            pos = pos + 1
    return found


def ordered_linear_search(num_list, num):
    """ Linear Search function for Ordered Lists """
    found = False
    stop = False
    pos = 0
    while pos < len(num_list) and not found and not stop:
        if num_list[pos] == num:
            found = True
        else:
            if num_list[pos] > num:
                stop = True
            else:
                pos = pos + 1
    return found


def main():
    num_list = [2, 4, 6, 8, 10]
    print(unordered_linear_search(num_list, 2))
    print(unordered_linear_search(num_list, 1))
    print(ordered_linear_search(num_list, 2))
    print(ordered_linear_search(num_list, 5))


if __name__ == "__main__":
    main()
