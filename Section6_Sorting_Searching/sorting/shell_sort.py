def shell_sort(num_list):
    """ Shell Sort Algorithm """

    # Sets initial list gap
    sublist_gap = len(num_list) // 2

    # Changes list gap
    while sublist_gap > 0:

        # Move the start position for the list gap
        for start_position in range(sublist_gap):
            # Insertion Sort for a sublist with a gap
            gap_insertion_sort(num_list, start_position, sublist_gap)

        # print("After increments of size: {} , sublist is: {}".format(
        #   sublist_gap, num_list))

        # Reduces list gap
        sublist_gap //= 2


def gap_insertion_sort(num_list, start, gap):
    """ Insertion Sort with Gap """

    # Creates sublists for the sublist gap
    for i in range(start + gap, len(num_list), gap):

        # New item to be inserted into the sublist gap
        current_value = num_list[i]
        position = i

        while position >= gap and num_list[position - gap] > current_value:
            # Shift item to current position
            num_list[position] = num_list[position - gap]
            position -= gap

        # Sets new position to current value
        num_list[position] = current_value


def main():
    num_list = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    shell_sort(num_list)
    print(num_list)

    charlist = list("PYTHON")
    shell_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
