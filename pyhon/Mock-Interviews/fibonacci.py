n=12

def fibonacci_recursion(n):
    if n < 0:
        return "n be a positive ."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
    
fibonacci_recursion = fibonacci_recursion(n)
print(fibonacci_recursion)


def fibonacci_for_loop(n):
    if n < 0:
        return "Invalid input. N must be a positive integer."
    fib_sequence = [0, 1]

    if n == 2:
        return fib_sequence[n - 1]

    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)

    return fib_sequence[-1]

fibonacci_for_loop = fibonacci_for_loop(n)
print(fibonacci_for_loop)