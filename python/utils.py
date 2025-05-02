# pylint: disable=line-too-long
"""
Utility functions to assist with solving Project Euler problems.
"""

from functools import wraps
import time
import math


def profiler(func):
    """
    A decorator to measure and log the execution time of a function.
    
    This decorator wraps the provided function and tracks the time it takes 
    to execute. The measured execution time is printed to the console 
    with a timestamp.

    Args:
        func (function): The function whose execution time needs to be measured.

    Returns:
        function: A wrapped version of the input function, which logs the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time() # Record the start time of the function call
        result = func(*args, **kwargs) # Execute the original function
        elapsed_time = time.time() - start_time # Compute the elapsed time
        print(f"Execution time of '{func.__name__}': {elapsed_time:.4f} seconds")
        return result

    return wrapper


def is_prime(n):
    """
    Determine if a number is prime.

    A prime number is a natural number greater than 1 that cannot be divided 
    evenly by any other numbers except for 1 and itself. This function efficiently 
    checks for primality by testing divisibility up to the square root of the given number.

    Args:
        n (int): The integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False # Numbers less than or equal to 1 are not prime
    if n == 2 or n == 3:
        return True # 2 and 3 are prime numbers
    if n % 2 == 0:
        return False # Exclude even numbers greater than 2

    # Check for divisibility from 3 up to the square root of n, skipping even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_atkin(limit):
    """
    Generates all prime numbers up to a given limit using the Sieve of Atkin method.
    
    The Sieve of Atkin is an optimized prime number generation algorithm that is faster 
    than the traditional Sieve of Eratosthenes for large numbers. The function generates 
    primes by checking possible values for a given limit, and uses modular arithmetic 
    to filter out non-prime numbers.
    
    Args:
        limit (int): The upper bound up to which prime numbers will be generated.
        
    Returns:
        list[int]: A list of prime numbers up to the specified limit.
    """
    sieve = [False] * (limit + 1)  # Initialize a sieve array to mark non-primes
    primes = [2, 3]

    # Sieve algorithm to mark prime candidates
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    # Eliminate numbers which are divisible by perfect squares of primes
    for n in range(5, int(math.sqrt(limit)) + 1):
        if sieve[n]:
            for k in range(n**2, limit + 1, n**2):
                sieve[k] = False

    # Collect all primes less than or equal to the limit
    for n in range(5, limit + 1):
        if sieve[n]:
            primes.append(n)

    return primes
