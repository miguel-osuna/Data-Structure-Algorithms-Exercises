# Bubble Sort Algorithm
def bubble_sort(num_list):
    """ Bubble Sort Algorithm """
    for passnum in range(len(num_list) - 1, 0, -1):
        for i in range(passnum):
            # Exchanges items
            if num_list[i] > num_list[i + 1]:
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp


def short_bubble_sort(num_list):
    """ Bubble Sort Algorithm with Interruption """
    exchange = True
    passnum = len(num_list) - 1

    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            # Exchanges items
            if num_list[i] > num_list[i + 1]:
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp
                exchange = True
        passnum -= 1


def cocktail_sort(num_list):
    """ Cocktail Sort Algorithm Implementation (Bubble Sort Variation) """

    # Setting variables
    start_index = 0
    end_index = len(num_list) - 1
    swapped = True

    while swapped:

        # Pass moves up
        swapped = False
        for i in range(start_index, end_index, 1):
            # Exchanges items
            if num_list[i] > num_list[i + 1]:
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp
                swapped = True
        end_index -= 1

        # Pass moves down
        swapped = False
        for i in range(end_index, start_index, -1):
            # Exchanges items
            if num_list[i] < num_list[i - 1]:
                temp = num_list[i]
                num_list[i] = num_list[i - 1]
                num_list[i - 1] = temp
                swapped = True
        start_index += 1


def main():
    num_list = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    bubble_sort(num_list)
    print(num_list)

    num_list2 = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    short_bubble_sort(num_list2)
    print(num_list2)

    numlist3 = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    print(numlist3)
    cocktail_sort(numlist3)
    print(numlist3)

    charlist = list("PYTHON")
    short_bubble_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
