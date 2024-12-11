"""
Generates the first n prime numbers
and saves them to a txt file
"""

# Import(s)
import time

# calc_primes function
def calc_primes():
    # Set customizable var(s)
    num_of_primes = 15000

    # Set a list of primes with the first prime (2)
    prime_li = [2]

    # Set num to first prime (2)
    num = 2

    # Continue until n amount of primes are found
    while len(prime_li) < num_of_primes:
        num += 1

        # Iterate through each prime
        for prime in prime_li:
            if num % prime == 0:
                break

        # If broken num is prime
        else:
            prime_li.append(num)

    # Return list of primes
    return prime_li


# calc_time function
def calc_time(func):
    start_time = time.time()
    var = func()
    end_time = time.time()
    return var, end_time - start_time


# Main function
def main():

    # Call calc_primes function
    prime_li = calc_time(calc_primes)

    # Print prime_li
    print(prime_li[0])
    print(prime_li[1])


# Call main function
main()