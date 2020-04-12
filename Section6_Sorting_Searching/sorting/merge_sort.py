def merge_sort(num_list):
    """ Merge Sort Algorithm """

    # Base and Recursive Case
    if len(num_list) > 1:
        mid = len(num_list) // 2

        # Creates sublists
        left_half = num_list[:mid]
        right_half = num_list[mid:]

        # Calls merge_sort for each sublist
        merge_sort(left_half)
        merge_sort(right_half)

        # Index for num_list, left_half list and right_half list respectively
        k = 0
        i = 0
        j = 0

        # Merges left_half and right_half in num_list
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                num_list[k] = left_half[i]
                i += 1
            else:
                num_list[k] = right_half[j]
                j += 1
            k += 1

        # Assigns remainder items from left_half list to num_list
        while i < len(left_half):
            num_list[k] = left_half[i]
            i += 1
            k += 1

        # Assigns remainder items from right_half list to num_list
        while j < len(right_half):
            num_list[k] = right_half[j]
            j += 1
            k += 1


def merge_sorth_in_place(num_list, start_index, end_index):
    """ Merge Sort In-Place Algorithm """
    pass


def main():
    num_list = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    merge_sort(num_list)
    print(num_list)

    charlist = list("PYTHON")
    merge_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
