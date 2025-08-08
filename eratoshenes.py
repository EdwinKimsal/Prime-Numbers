"""
This file includes the code to find all prime numbers
up to n value. This algorithm is called the Sieve of
Eratosthenes, which is an ancient algorithm
"""


# Import(s)
import os
import time


# Function to write lines from array into txt file
def write_output(file, li):
    with open(file, "w") as f:
        for line in li:
            f.writelines(str(line) + "\n")


# Main function
def main():
    n = 100 # Inclusively test up to this number for primes (must be greater than 1)
    outpath = os.path.join(os.getcwd(), "primes.txt")

    # Start time
    start_time = time.perf_counter()

    # Add numbers to list
    primes = []
    is_prime = [True for num in range(0, n+1)]

    curr = 2
    while curr*curr <= n:
        if is_prime[curr]:
            for mult in range(curr*curr, n+1, curr):
                is_prime[mult] = False
        curr += 1

    for index in range(2, len(is_prime)):
        if is_prime[index]:
            primes.append(index)

    # Call function to write array in outfile
    write_output(outpath, primes)

    # Calculate time
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"{elapsed_time} seconds")


# Call main function
main()