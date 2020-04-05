def quickSort(numlist):
    """ Quick Sort Algorithm """

    startIndex = 0
    endIndex = len(numlist) - 1
    quickSortRec(numlist, startIndex, endIndex)


def quickSortRec(numlist, startIndex, endIndex):
    """ Quick Sort Recursion Algorithm """

    # Base Case
    # Checks if the partition segment is valid
    if startIndex < endIndex:
        pivotIndex = makePartition(numlist, startIndex, endIndex)
        quickSortRec(numlist, startIndex, pivotIndex - 1)
        quickSortRec(numlist, pivotIndex + 1, endIndex)


def makePartition(numlist, startIndex, endIndex):
    """ List Partitioning Function """

    # Sets pivot
    pivot = numlist[endIndex]
    pivotIndex = startIndex

    # Loop through the partition segment
    for index in range(startIndex, endIndex, 1):
        if numlist[index] <= pivot:
            # Swaps items
            temp = numlist[index]
            numlist[index] = numlist[pivotIndex]
            numlist[pivotIndex] = temp

            # Moves pivot index
            pivotIndex += 1

    # Moves pivot to pivotIndex location
    temp = numlist[pivotIndex]
    numlist[pivotIndex] = pivot
    numlist[endIndex] = temp

    return pivotIndex


if __name__ == "__main__":
    numlist = [7, 2, 1, 6, 8, 5, 3, 4]
    quickSort(numlist)
    print(numlist)

    charlist = list("PYTHON")
    quickSort(charlist)
    print(charlist)
