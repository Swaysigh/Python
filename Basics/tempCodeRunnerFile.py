def fibonacci(n):
    fib_sequence = [0, 1]  # Start with the first two Fibonacci numbers
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])  # Sum of the previous two numbers
    return fib_sequence  # Return the sequence up to the nth number

# Example usage
n = 10
print(fibonacci(n))