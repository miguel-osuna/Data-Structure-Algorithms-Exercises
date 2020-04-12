# Standard library imports
import timeit

# Local application imports
from queue1 import Queue1
from queue2 import Queue2


def test_enqueue():
    """ Enqueue testing"""

    # Enqueue statements and setups
    estmt1 = "for i in range(1, 10): q1.enqueue(i)"
    estmt2 = "for i in range(1, 10): q2.enqueue(i)"

    esetup1 = "from __main__ import Queue1; q1 = Queue1()"
    esetup2 = "from __main__ import Queue2; q2 = Queue2()"

    test_eq1 = timeit.Timer(estmt1, esetup1)
    test_eq2 = timeit.Timer(estmt2, esetup2)

    print("Queue1.enqueue =>", test_eq1.timeit(number=1000), "seconds")
    print("Queue2.enqueue =>", test_eq2.timeit(number=1000), "seconds")


def test_dequeue():
    """ Dequeu testing """

    # Dequeue statements and setups
    dstmt1 = "for _ in range(1, 100): q1.dequeue()"
    dstmt2 = "for _ in range(1, 100): q2.dequeue()"

    dsetup1 = "from __main__ import Queue1; q1 = Queue1(); l = [q1.enqueue(i) for i in range(1, 100000)]"
    dsetup2 = "from __main__ import Queue2; q2 = Queue2(); l = [q2.enqueue(i) for i in range(1, 100000)]"

    test_deq1 = timeit.Timer(dstmt1, dsetup1)
    test_deq2 = timeit.Timer(dstmt2, dsetup2)

    print("Queue1.dequeue =>", test_deq1.timeit(number=1000), "seconds")
    print("Queue2.dequeue =>", test_deq2.timeit(number=1000), "seconds")


def main():
    test_enqueue()
    test_dequeue()


if __name__ == "__main__":
    main()
