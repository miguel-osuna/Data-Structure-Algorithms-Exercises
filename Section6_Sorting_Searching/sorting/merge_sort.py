def mergeSort(numlist):
    ''' Merge Sort Algorithm '''

    # Base and Recursive Case
    if len(numlist) > 1:
        mid = len(numlist) // 2

        # Creates sublists
        lefthalf = numlist[:mid]
        righthalf = numlist[mid:]

        # Calls mergeSort for each sublist
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # Index for numlist, lefthalf list and righthalf list respectively
        k = 0
        i = 0
        j = 0

        # Merges lefthalf and righthalf in numlist
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                numlist[k] = lefthalf[i]
                i += 1
            else:
                numlist[k] = righthalf[j]
                j += 1
            k += 1

        # Assigns remainder items from lefthalf list to numlist
        while i < len(lefthalf):
            numlist[k] = lefthalf[i]
            i += 1
            k += 1

        # Assigns remainder items from righthalf list to numlist
        while j < len(righthalf):
            numlist[k] = righthalf[j]
            j += 1
            k += 1


def mergeSortInPlace(numlist, start, end):
    ''' Merge Sort In-Place Algorithm '''
    pass


if __name__ == "__main__":
    numlist = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    mergeSort(numlist)
    print(numlist)

    charlist = list("PYTHON")
    mergeSort(charlist)
    print(charlist)
