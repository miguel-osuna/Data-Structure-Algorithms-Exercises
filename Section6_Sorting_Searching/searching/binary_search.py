def binary_search(num_list, num):
    """ Binary Search Function """
    start = 0
    end = len(num_list) - 1
    found = False

    while start <= end and not found:
        midpoint = (start + end) // 2
        if num_list[midpoint] == num:
            found = True
        else:
            if num_list[midpoint] < num:
                start = midpoint + 1
            else:
                end = midpoint - 1

    return found


def binary_search_rec(num_list, num):
    """ Recursive Binary Search Function """
    if len(num_list) == 0:
        return False
    else:
        midpoint = len(num_list) // 2
        if num_list[midpoint] == num:
            return True
        else:
            if num_list[midpoint] > num:
                return binary_search_rec(num_list[:midpoint], num)
            else:
                return binary_search_rec(num_list[midpoint + 1 :], num)


def binary_search_rec_in_place(num_list, start_index, end_index, num):
    """ Recursive Binary Search In-Place Function """
    if (end_index - start_index) == 0:
        return False

    else:
        midpoint = (end_index + start_index) // 2
        if num_list[midpoint] == num:
            return True

        else:
            if num_list[midpoint] > num:
                return binary_search_rec_in_place(
                    num_list, start_index, midpoint - 1, num
                )
            else:
                return binary_search_rec_in_place(
                    num_list, midpoint + 1, end_index, num
                )


def main():
    num_list = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    num = 54
    print(binary_search(num_list, num))
    print(binary_search_rec(num_list, num))
    print(binary_search_rec_in_place(num_list, 0, len(num_list) - 1, num))


if __name__ == "__main__":
    main()
