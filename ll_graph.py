"""
This file graphs the results of lucas-lehmer
sequence after each iteration for some prime (p)
"""


# Import(s)
import os
import time
import matplotlib.pyplot as plt


# Function to make graph of all s values for p
def make_graph(p, val):
    plt.title(str(p))
    plt.xlabel("Iteration")
    plt.ylabel("Remainder")
    plt.plot(range(1, len(val)+1), val)
    plt.grid()
    plt.show()


# Function to write lines from array into txt file
def write_output(file, li):
    with open(file, "w") as f:
        for line in li:
            f.writelines(str(line) + "\n")


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
    # Create a blank file for points
    points = []

    # Iterate for how big p is or when formula equals 0
    while iteration <= p:
        # Append s (remainder) to points
        points.append(s)

        # Calculate current s and see if 0 (then prime, else not yet prime)
        s = (s**2-2) % m
        if s == 0:
            points.append(s)
            return True, points
        iteration += 1
    return False, points


# Main function
def main():
    # Customizable variables
    n = 100
    input_file = os.path.join(os.getcwd(), "Tests", "one-billion.txt")

    # Start time
    start_time = time.perf_counter()

    # Get a list of all primes less than or equal to an n value
    p_list = get_primes(n, input_file)

    # Set a blank list to store mersenne numbers
    p_primes = [2]

    # Append all mersenne primes
    for p in p_list:
        return_value = is_prime_check(2**p-1, p, 4, 1)
        if return_value[0]:
            p_primes.append(p)
        make_graph(p, return_value[1])

    # Display primes
    print(p_primes)

    # Calculate time
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"{elapsed_time} seconds")


# Call main function
main()