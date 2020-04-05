def insertionSort(numlist):
    """ Insertion Sort Algorithm """
    for index in range(1, len(numlist)):

        # New item to be inserted into the sublist
        currentValue = numlist[index]
        position = index

        # Sweeps sublist from end to beginning
        while position > 0 and numlist[position - 1] > currentValue:
            # Shifting item to current position
            numlist[position] = numlist[position - 1]
            position -= 1

        # Sets new position to the current value
        numlist[position] = currentValue


def main():
    numlist = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    insertionSort(numlist)
    print(numlist)

    charlist = list("PYTHON")
    insertionSort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
