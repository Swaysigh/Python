# A Common Example of Recursion Is Factorial Function 
# As we are calling the factorial function inside the function itself

def factorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num-1))
    
num = 5
print("Number = ", num)
print("Factorial = " ,factorial(num))    

#fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]  # Start with the first two Fibonacci numbers
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])  # Sum of the previous two numbers
    return fib_sequence  # Return the sequence up to the nth number

# Example usage
n = 10
print(fibonacci(n))
