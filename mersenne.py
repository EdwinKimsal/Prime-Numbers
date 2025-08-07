"""
This file detects mersenne prime numbers, where the
input file is a list of prime numbers with each new
line being the next prime number. The algorithm used
is the Lucas-Lehmer sequence.
"""

# Import(s)
import os
import time

# Function to get primes upto some n value
def get_primes(n, file):
    primes = [] # Initialize a blank list to store primes

    # Collect n primes from file with primes
    with open(file, "r") as f:
        for num in f:
            if int(num) <= n:
                primes.append(int(num))
            else:
                break
    return primes


# Function to test if mersenne number is prime
def is_prime_check(m, p, s, iteration):
    # Iterate for how big p is or when formula equals 0
    if iteration <= p:
        if iteration == 0:
            s_iter = 4
        else:
            s_iter = (s**2-2) % m
        if s_iter == 0:
            return True
        else:
            return is_prime_check(m, p, s_iter, iteration+1)
    else:
        return False


# Main function
def main():
    # Customizable variables
    n = 2500
    input_file = os.path.join(os.getcwd(), "Tests", "one-billion.txt")

    # Start time
    start_time = time.perf_counter()

    # Get a list of all primes less than or equal to an n value
    p_list = get_primes(n, input_file)

    # Set a blank list to store mersenne numbers
    p_primes = [2]

    # Append all mersenne primes
    for p in p_list:
        if is_prime_check(2**p-1, p, 4, 0):
            p_primes.append(p)

    # Display mersenne primes
    print(p_primes)

    # Calculate time
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"{elapsed_time} seconds")


# Call main function
main()