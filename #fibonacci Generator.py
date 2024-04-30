#fibonacci Generator
def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]  
    while True:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_num <= limit:
            fibonacci_sequence.append(next_num)
        else:
            break
    return fibonacci_sequence

limit = int(input("Enter the limit for Fibonacci sequence: "))
fib_sequence = generate_fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", fib_sequence)
