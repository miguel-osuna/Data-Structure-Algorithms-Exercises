def insertion_sort(num_list):
    """ Insertion Sort Algorithm """
    for index in range(1, len(num_list)):

        # New item to be inserted into the sublist
        current_value = num_list[index]
        position = index

        # Sweeps sublist from end to beginning
        while position > 0 and num_list[position - 1] > current_value:
            # Shifting item to current position
            num_list[position] = num_list[position - 1]
            position -= 1

        # Sets new position to the current value
        num_list[position] = current_value


def main():
    num_list = [345, 23, 54, 64, 98, 22, 45, 18, 78]
    insertion_sort(num_list)
    print(num_list)

    charlist = list("PYTHON")
    insertion_sort(charlist)
    print(charlist)


if __name__ == "__main__":
    main()
