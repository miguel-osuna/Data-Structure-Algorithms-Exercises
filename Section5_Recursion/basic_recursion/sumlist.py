# Non recursive sum list solution
def sumList(numList):
    total = 0
    for num in numList:
        total += num
    return total


# Recursive sum list solution
def sumListRecursion(numList):

    # Base Case
    if len(numList) == 1:
        return numList[0]

    # Recursive Case
    else:
        return numList[0] + sumListRecursion(numList[1:])


if __name__ == "__main__":
    numlist = [1, 2, 3, 4, 5]
    print(sumList(numlist))
    print(sumListRecursion(numlist))
