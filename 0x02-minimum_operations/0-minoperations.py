#!/usr/bin/python3

def minOperations(n):
    # If n is less than or equal to 1, it's impossible to achieve, so return 0
    if n <= 1:
        return 0
    # Initialize the number of operations needed to 0
    operations = 0
    # Start checking for divisors from 2 onwards
    divisor = 2
    # Continue the loop until n is reduced to 1
    while n > 1:
        # Check if the current divisor can divide n
        while n % divisor == 0:
            # If it can, add the divisor to the total number of operations
            operations += divisor
            # Divide n by the divisor to reduce it
            n //= divisor
        # Move to the next possible divisor
        divisor += 1
    # Return the total number of operations needed to reach n
    return operations
