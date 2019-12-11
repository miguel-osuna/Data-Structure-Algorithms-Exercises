import time

# Implementing Sequential Sum


def sumOfN(n):
    start = time.time()

    sum = 0
    for i in range(1, n + 1):
        sum = sum + i

    end = time.time()

    return sum, end - start


print("Implementing sequential sum")

for _ in range(5):
    print("Sum is: %d, required: %10.7f seconds" % sumOfN(10000))

for _ in range(5):
    print("Sum is: %d, required: %10.7f seconds" % sumOfN(100000))

for _ in range(5):
    print("Sum is: %d, required: %10.7f seconds" % sumOfN(1000000))

# Implementing Gauss Sum


def sumOfN2(n):
    start = time.time()
    sum = (n * (n - 1)) / 2
    end = time.time()
    return sum, end - start


print("Execution Time of Gauss Sum")

for _ in range(5):
    print("Sum is: %d, required: %10.7f seconds" % sumOfN2(10000))

for _ in range(5):
    print("Sum is: %d, required: %10.7f seconds" % sumOfN2(100000))

for _ in range(5):
    print("Sum is: %d, required: %10.7f seconds" % sumOfN2(1000000))



