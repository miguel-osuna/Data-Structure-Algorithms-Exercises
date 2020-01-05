import timeit
import random
from linear_search import unorderedLinearSearch, orderedLinearSearch
from binary_search import binarySearch


def test_unorderedLinearSearch():
    # Statements and setup
    statement = "for i in range(100): unorderedLinearSearch(numlist, i)"
    setup = "from __main__ import unorderedLinearSearch; from __main__ import random; numlist = sorted([random.randint(0, 100) for _ in range(100)])"

    # Testing and timing 
    test = timeit.Timer(statement, setup)
    print("unorderedLinearSearch() =>", test.timeit(number=1000), "seconds")

def test_orderedLinearSearch():
    # Statements and setup
    statement = "for i in range(100): orderedLinearSearch(numlist, i)"
    setup = "from __main__ import orderedLinearSearch; from __main__ import random; numlist = sorted([random.randint(0, 100) for _ in range(100)])"

    # Testing and timing 
    test = timeit.Timer(statement, setup)
    print("orderedLinearSearch() =>", test.timeit(number=1000), "seconds")

def test_binarySearch():
    # Statement and setup for binary search
    statement = "for i in range(100): binarySearch(numlist, i)"
    setup = "from __main__ import binarySearch; from __main__ import random; numlist = sorted([random.randint(0, 100) for _ in range(100)])"

    # Testing and timing
    test = timeit.Timer(statement, setup)
    print("binarySearch() =>", test.timeit(number=1000), "seconds")

test_unorderedLinearSearch()
test_orderedLinearSearch()
test_binarySearch()