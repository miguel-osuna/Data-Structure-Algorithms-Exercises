def binarySearch(numlist, num):
    ''' Binary Search Function '''
    start = 0
    end = len(numlist) - 1
    found = False

    while start <= end and not found:
        midpoint = (start + end) // 2
        if numlist[midpoint] == num:
            found = True
        else:
            if numlist[midpoint] < num:
                start = midpoint + 1
            else:
                end = midpoint - 1

    return found


def binarySearchRec(numlist, num):
    ''' Recursive Binary Search Function '''
    if len(numlist) == 0:
        return False
    else:
        midpoint = len(numlist) // 2
        if numlist[midpoint] == num:
            return True
        else:
            if numlist[midpoint] > num:
                return binarySearchRec(numlist[:midpoint], num)
            else:
                return binarySearchRec(numlist[midpoint+1:], num)


def binarySearchRecInPlace(numlist, startIndex, endIndex, num):
    ''' Recursive Binary Search In-Place Function '''
    if (endIndex - startIndex) == 0:
        return False

    else:
        midpoint = (endIndex + startIndex) // 2
        if numlist[midpoint] == num:
            return True

        else:
            if numlist[midpoint] > num:
                return binarySearchRecInPlace(numlist, startIndex, midpoint - 1, num)
            else:
                return binarySearchRecInPlace(numlist, midpoint + 1, endIndex, num)


if __name__ == "__main__":
    numlist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    num = 54
    print(binarySearch(numlist, num))
    print(binarySearchRec(numlist, num))
    print(binarySearchRecInPlace(numlist, 0, len(numlist) - 1, num))
