#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    fibonacci = [0, 1]
    
    for _ in range(2, length):
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)
    
    print(fibonacci)