import timeit
import random
from linear_search import unordered_linear_search, ordered_linear_search
from binary_search import binary_search


def test_unordered_linear_search():
    # Statements and setup
    statement = "for i in range(100): unordered_linear_search(numlist, i)"
    setup = "from __main__ import unordered_linear_search; from __main__ import random; numlist = sorted([random.randint(0, 100) for _ in range(100)])"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("unordered_linear_search() =>", test.timeit(number=1000), "seconds")


def test_ordered_linear_search():
    # Statements and setup
    statement = "for i in range(100): ordered_linear_search(numlist, i)"
    setup = "from __main__ import ordered_linear_search; from __main__ import random; numlist = sorted([random.randint(0, 100) for _ in range(100)])"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("ordered_linear_search() =>", test.timeit(number=1000), "seconds")


def test_binary_search():
    # Statement and setup for binary search
    statement = "for i in range(100): binary_search(numlist, i)"
    setup = "from __main__ import binary_search; from __main__ import random; numlist = sorted([random.randint(0, 100) for _ in range(100)])"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("binary_search() =>", test.timeit(number=1000), "seconds")


def main():
    test_unordered_linear_search()
    test_ordered_linear_search()
    test_binary_search()


if __name__ == "__main__":
    main()
