def binary_search(numlist, num):
    """ Binary Search Function """
    start = 0
    end = len(numlist) - 1
    found = False

    while start <= end and not found:
        midpoint = (start + end) // 2
        if numlist[midpoint] == num:
            found = True
        else:
            if numlist[midpoint] < num:
                start = midpoint + 1
            else:
                end = midpoint - 1

    return found


def binary_search_rec(numlist, num):
    """ Recursive Binary Search Function """
    if len(numlist) == 0:
        return False
    else:
        midpoint = len(numlist) // 2
        if numlist[midpoint] == num:
            return True
        else:
            if numlist[midpoint] > num:
                return binary_search_rec(numlist[:midpoint], num)
            else:
                return binary_search_rec(numlist[midpoint + 1 :], num)


def binary_search_rec_in_place(numlist, start_index, end_index, num):
    """ Recursive Binary Search In-Place Function """
    if (end_index - start_index) == 0:
        return False

    else:
        midpoint = (end_index + start_index) // 2
        if numlist[midpoint] == num:
            return True

        else:
            if numlist[midpoint] > num:
                return binary_search_rec_in_place(
                    numlist, start_index, midpoint - 1, num
                )
            else:
                return binary_search_rec_in_place(numlist, midpoint + 1, end_index, num)


def main():
    numlist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    num = 54
    print(binary_search(numlist, num))
    print(binary_search_rec(numlist, num))
    print(binary_search_rec_in_place(numlist, 0, len(numlist) - 1, num))


if __name__ == "__main__":
    main()
