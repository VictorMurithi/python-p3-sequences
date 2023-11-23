#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        return "[]\n"
    
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    # Print the Fibonacci sequence in the expected format
    print("Fibonacci sequence:", fibonacci_sequence)

    return fibonacci_sequence
    # rest of the function implementation
