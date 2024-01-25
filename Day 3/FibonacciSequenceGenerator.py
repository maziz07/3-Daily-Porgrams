def fibonacci(n):
    a, b = 0, 1
    sequence = []
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Test the function
n = 100  # Generate Fibonacci numbers up to 100
print(f"Fibonacci sequence up to {n}: {fibonacci(n)}")
