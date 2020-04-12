# Standard library imports
import timeit
import random

# Local application imports
from bubble_sort import bubble_sort
from bubble_sort import short_bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def test_bubble_sort():
    """ Tests bubble sort algorithm """
    statement = "bubble_sort(num_list)"
    setup = "from __main__ import bubble_sort; from __main__ import random; num_list = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("bubble_sort() =>", test.timeit(number=1000), "seconds")


def test_short_bubble_sort():
    """ Tests short bubble sort algorithm """
    statement = "short_bubble_sort(num_list)"
    setup = "from __main__ import short_bubble_sort; from __main__ import random; num_list = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("short_bubble_sort() =>", test.timeit(number=1000), "seconds")


def test_selection_sort():
    """ Tests selection sort algorithm """
    statement = "selection_sort(num_list)"
    setup = "from __main__ import selection_sort; from __main__ import random; num_list = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("selection_sort() =>", test.timeit(number=1000), "seconds")


def test_insertion_sort():
    """ Tests insertion sort algorithm """
    # Statement and setup
    statement = "insertion_sort(num_list)"
    setup = "from __main__ import insertion_sort; from __main__ import random; num_list = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("insertion_sort() =>", test.timeit(number=1000), "seconds")


def test_shell_sort():
    """ Tests shell sort algorithm """
    # Statement and setup
    statement = "shell_sort(num_list)"
    setup = "from __main__ import shell_sort; from __main__ import random; num_list = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("shell_sort() =>", test.timeit(number=1000), "seconds")


def test_merge_sort():
    """ Tests merge sort algorithm """
    # Statement and setup
    statement = "merge_sort(num_list)"
    setup = "from __main__ import merge_sort; from __main__ import random; num_list = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("merge_sort() =>", test.timeit(number=1000), "seconds")


def test_quick_sort():
    """ Tests quick sort algorithm """
    # Statement and setup
    statement = "quick_sort(num_list)"
    setup = "from __main__ import quick_sort; from __main__ import random; num_list = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("quick_sort() =>", test.timeit(number=1000), "seconds")


def main():
    """ Tests sorting algorithms """
    test_bubble_sort()
    test_short_bubble_sort()
    test_selection_sort()
    test_insertion_sort()
    test_shellSort()
    test_mergeSort()
    test_quickSort()


if __name__ == " __main__":
    main()
