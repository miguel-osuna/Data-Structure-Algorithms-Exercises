# Non recursive sum list solution
def sum_list(numList):
    total = 0
    for num in numList:
        total += num
    return total


# Recursive sum list solution
def sum_list_recursion(numList):

    # Base Case
    if len(numList) == 1:
        return numList[0]

    # Recursive Case
    else:
        return numList[0] + sum_list_recursion(numList[1:])


def main():
    numlist = [1, 2, 3, 4, 5]
    print(sum_list(numlist))
    print(sum_list_recursion(numlist))


if __name__ == "__main__":
    main()
