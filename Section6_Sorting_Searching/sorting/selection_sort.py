def selection_sort(numlist):
    """ Selection Sort Algorithm """

    # Sweeps through the list decreasingly
    for fillslot in range(len(numlist) - 1, 0, -1):
        max_num_pos = 0

        # Sweeps the list
        for i in range(1, fillslot + 1):
            # Sets new position for largest number
            if numlist[i] > numlist[max_num_pos]:
                max_num_pos = i

        # Exchanges items
        temp = numlist[fillslot]
        numlist[fillslot] = numlist[max_num_pos]
        numlist[max_num_pos] = temp


def main():
    numlist = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    selection_sort(numlist)
    print(numlist)

    charlist = list("PYTHON")
    selection_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
