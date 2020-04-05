def shellSort(numlist):
    """ Shell Sort Algorithm """

    # Sets initial list gap
    sublistgap = len(numlist) // 2

    # Changes list gap
    while sublistgap > 0:

        # Move the start position for the list gap
        for startposition in range(sublistgap):
            # Insertion Sort for a sublist with a gap
            gapInsertionSort(numlist, startposition, sublistgap)

        # print("After increments of size: {} , sublist is: {}".format(
        #   sublistgap, numlist))

        # Reduces list gap
        sublistgap //= 2


def gapInsertionSort(numlist, start, gap):
    """ Insertion Sort with Gap """

    # Creates sublists for the sublist gap
    for i in range(start + gap, len(numlist), gap):

        # New item to be inserted into the sublist gap
        currentValue = numlist[i]
        position = i

        while position >= gap and numlist[position - gap] > currentValue:
            # Shift item to current position
            numlist[position] = numlist[position - gap]
            position -= gap

        # Sets new position to current value
        numlist[position] = currentValue


if __name__ == "__main__":
    numlist = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    shellSort(numlist)
    print(numlist)

    charlist = list("PYTHON")
    shellSort(charlist)
    print(charlist)
