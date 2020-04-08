def shell_sort(numlist):
    """ Shell Sort Algorithm """

    # Sets initial list gap
    sublist_gap = len(numlist) // 2

    # Changes list gap
    while sublist_gap > 0:

        # Move the start position for the list gap
        for start_position in range(sublist_gap):
            # Insertion Sort for a sublist with a gap
            gap_insertion_sort(numlist, start_position, sublist_gap)

        # print("After increments of size: {} , sublist is: {}".format(
        #   sublist_gap, numlist))

        # Reduces list gap
        sublist_gap //= 2


def gap_insertion_sort(numlist, start, gap):
    """ Insertion Sort with Gap """

    # Creates sublists for the sublist gap
    for i in range(start + gap, len(numlist), gap):

        # New item to be inserted into the sublist gap
        current_value = numlist[i]
        position = i

        while position >= gap and numlist[position - gap] > current_value:
            # Shift item to current position
            numlist[position] = numlist[position - gap]
            position -= gap

        # Sets new position to current value
        numlist[position] = current_value


def main():
    numlist = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    shell_sort(numlist)
    print(numlist)

    charlist = list("PYTHON")
    shell_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
