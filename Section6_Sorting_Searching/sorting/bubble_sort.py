# Bubble Sort Algorithm
def bubbleSort(numlist):
    """ Bubble Sort Algorithm """
    for passnum in range(len(numlist) - 1, 0, -1):
        for i in range(passnum):
            # Exchanges items
            if numlist[i] > numlist[i + 1]:
                temp = numlist[i]
                numlist[i] = numlist[i + 1]
                numlist[i + 1] = temp


def shortBubbleSort(numlist):
    """ Bubble Sort Algorithm with Interruption """
    exchange = True
    passnum = len(numlist) - 1

    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            # Exchanges items
            if numlist[i] > numlist[i + 1]:
                temp = numlist[i]
                numlist[i] = numlist[i + 1]
                numlist[i + 1] = temp
                exchange = True
        passnum -= 1


def cocktailSort(numlist):
    """ Cocktail Sort Algorithm Implementation (Bubble Sort Variation) """

    # SEtting variables
    startIndex = 0
    endIndex = len(numlist) - 1
    swapped = True

    while swapped:

        # Pass moves up
        swapped = False
        for i in range(startIndex, endIndex, 1):
            # Exchanges items
            if numlist[i] > numlist[i + 1]:
                temp = numlist[i]
                numlist[i] = numlist[i + 1]
                numlist[i + 1] = temp
                swapped = True
        endIndex -= 1

        # Pass moves down
        swapped = False
        for i in range(endIndex, startIndex, -1):
            # Exchanges items
            if numlist[i] < numlist[i - 1]:
                temp = numlist[i]
                numlist[i] = numlist[i - 1]
                numlist[i - 1] = temp
                swapped = True
        startIndex += 1


if __name__ == "__main__":
    numlist = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    bubbleSort(numlist)
    print(numlist)

    numlist2 = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    shortBubbleSort(numlist2)
    print(numlist2)

    numlist3 = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    print(numlist3)
    cocktailSort(numlist3)
    print(numlist3)

    charlist = list("PYTHON")
    shortBubbleSort(charlist)
    print(charlist)
