# Fibonacci Function integrated with Memoization
def fib_memoization(num, memo):
    if num <= 0:
        result = 0
    elif num == 1:
        result = 1
    elif memo[num] != None:
        result = memo[num]
    else:
        result = fib_memoization(num - 1, memo) + fib_memoization(num - 2, memo)
        memo[num] = result
    return result


# Decorator Memoize Function
def memoize(function):
    memo = {}

    def wrapper(x):
        if x not in memo:
            memo[x] = function(x)
        return memo[x]

    return wrapper


# Decorator Memoize Class
class Memoize:
    def __init__(self, function):
        self.function = function
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.function(*args)
        return self.memo[args]


@Memoize
def fibonacci(num):
    if num <= 0:
        result = 0
    elif num == 1:
        result = 1
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
    return result


def main():
    print(fibonacci(30))
    print(fibonacci(20))


if __name__ == "__main__":
    main()
