import timeit
import random
from bubble_sort import bubbleSort
from bubble_sort import shortBubbleSort
from selection_sort import selectionSort
from insertion_sort import insertionSort
from shell_sort import shellSort
from merge_sort import mergeSort
from quick_sort import quickSort


def test_bubbleSort():
    # Statement and setup
    statement = "bubbleSort(numlist)"
    setup = "from __main__ import bubbleSort; from __main__ import random; numlist = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("bubbleSort() =>", test.timeit(number=1000), "seconds")


def test_shortBubbleSort():
    # Statement and setup
    statement = "shortBubbleSort(numlist)"
    setup = "from __main__ import shortBubbleSort; from __main__ import random; numlist = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("shortBubbleSort() =>", test.timeit(number=1000), "seconds")


def test_selectionSort():
    # Statement and setup
    statement = "selectionSort(numlist)"
    setup = "from __main__ import selectionSort; from __main__ import random; numlist = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("selectionSort() =>", test.timeit(number=1000), "seconds")


def test_insertionSort():
    # Statement and setup
    statement = "insertionSort(numlist)"
    setup = "from __main__ import insertionSort; from __main__ import random; numlist = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("insertionSort() =>", test.timeit(number=1000), "seconds")


def test_shellSort():
    # Statement and setup
    statement = "shellSort(numlist)"
    setup = "from __main__ import shellSort; from __main__ import random; numlist = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("shellSort() =>", test.timeit(number=1000), "seconds")


def test_mergeSort():
    # Statement and setup
    statement = "mergeSort(numlist)"
    setup = "from __main__ import mergeSort; from __main__ import random; numlist = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("mergeSort() =>", test.timeit(number=1000), "seconds")


def test_quickSort():
    # Statement and setup
    statement = "quickSort(numlist)"
    setup = "from __main__ import quickSort; from __main__ import random; numlist = [random.randint(0, 500) for _ in range(500)]"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("quickSort() =>", test.timeit(number=1000), "seconds")


# Testing every sorting algorithm
test_bubbleSort()
test_shortBubbleSort()
test_selectionSort()
test_insertionSort()
test_shellSort()
test_mergeSort()
test_quickSort()
