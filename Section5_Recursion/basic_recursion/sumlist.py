# Non recursive sum list solution
def sum_list(num_list):
    """ Non recursive sum list solution """
    total = 0
    for num in num_list:
        total += num
    return total


def sum_list_recursion(num_list):
    """ Recursive sum list solution """

    # Base Case
    if len(num_list) == 1:
        return num_list[0]

    # Recursive Case
    else:
        return num_list[0] + sum_list_recursion(num_list[1:])


def main():
    num_list = [1, 2, 3, 4, 5]
    print(sum_list(num_list))
    print(sum_list_recursion(num_list))


if __name__ == "__main__":
    main()
