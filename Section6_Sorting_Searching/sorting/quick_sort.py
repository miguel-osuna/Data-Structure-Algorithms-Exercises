def quick_sort(numlist):
    """ Quick Sort Algorithm """

    start_index = 0
    end_index = len(numlist) - 1
    quick_sort_rec(numlist, start_index, end_index)


def quick_sort_rec(numlist, start_index, end_index):
    """ Quick Sort Recursion Algorithm """

    # Base Case
    # Checks if the partition segment is valid
    if start_index < end_index:
        pivot_index = make_partition(numlist, start_index, end_index)
        quick_sort_rec(numlist, start_index, pivot_index - 1)
        quick_sort_rec(numlist, pivot_index + 1, end_index)


def make_partition(numlist, start_index, end_index):
    """ List Partitioning Function """

    # Sets pivot
    pivot = numlist[end_index]
    pivot_index = start_index

    # Loop through the partition segment
    for index in range(start_index, end_index, 1):
        if numlist[index] <= pivot:
            # Swaps items
            temp = numlist[index]
            numlist[index] = numlist[pivot_index]
            numlist[pivot_index] = temp

            # Moves pivot index
            pivot_index += 1

    # Moves pivot to pivot_index location
    temp = numlist[pivot_index]
    numlist[pivot_index] = pivot
    numlist[end_index] = temp

    return pivot_index


def main():
    numlist = [7, 2, 1, 6, 8, 5, 3, 4]
    quick_sort(numlist)
    print(numlist)

    charlist = list("PYTHON")
    quick_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
