def selectionSort(numlist):
    ''' Selection Sort Algorithm '''

    # Sweeps through the list decreasingly
    for fillslot in range(len(numlist)-1, 0, -1):
        maxNumPos = 0

        # Sweeps the list
        for i in range(1, fillslot+1):
            # Sets new position for largest number
            if numlist[i] > numlist[maxNumPos]:
                maxNumPos = i

        # Exchanges items
        temp = numlist[fillslot]
        numlist[fillslot] = numlist[maxNumPos]
        numlist[maxNumPos] = temp


if __name__ == "__main__":
    numlist = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    selectionSort(numlist)
    print(numlist)

    charlist = list("PYTHON")
    selectionSort(charlist)
    print(charlist)
