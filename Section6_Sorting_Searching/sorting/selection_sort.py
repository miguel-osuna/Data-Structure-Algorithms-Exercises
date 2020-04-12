def selection_sort(num_list):
    """ Selection Sort Algorithm """

    # Sweeps through the list decreasingly
    for fill_slot in range(len(num_list) - 1, 0, -1):
        max_num_pos = 0

        # Sweeps the list
        for i in range(1, fill_slot + 1):
            # Sets new position for largest number
            if num_list[i] > num_list[max_num_pos]:
                max_num_pos = i

        # Exchanges items
        temp = num_list[fill_slot]
        num_list[fill_slot] = num_list[max_num_pos]
        num_list[max_num_pos] = temp


def main():
    num_list = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    selection_sort(num_list)
    print(num_list)

    charlist = list("PYTHON")
    selection_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
