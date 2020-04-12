def quick_sort(num_list):
    """ Quick Sort Algorithm """

    start_index = 0
    end_index = len(num_list) - 1
    quick_sort_rec(num_list, start_index, end_index)


def quick_sort_rec(num_list, start_index, end_index):
    """ Quick Sort Recursion Algorithm """

    # Base Case
    # Checks if the partition segment is valid
    if start_index < end_index:
        pivot_index = make_partition(num_list, start_index, end_index)
        quick_sort_rec(num_list, start_index, pivot_index - 1)
        quick_sort_rec(num_list, pivot_index + 1, end_index)


def make_partition(num_list, start_index, end_index):
    """ List Partitioning Function """

    # Sets pivot
    pivot = num_list[end_index]
    pivot_index = start_index

    # Loop through the partition segment
    for index in range(start_index, end_index, 1):
        if num_list[index] <= pivot:
            # Swaps items
            temp = num_list[index]
            num_list[index] = num_list[pivot_index]
            num_list[pivot_index] = temp

            # Moves pivot index
            pivot_index += 1

    # Moves pivot to pivot_index location
    temp = num_list[pivot_index]
    num_list[pivot_index] = pivot
    num_list[end_index] = temp

    return pivot_index


def main():
    num_list = [7, 2, 1, 6, 8, 5, 3, 4]
    quick_sort(num_list)
    print(num_list)

    charlist = list("PYTHON")
    quick_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
