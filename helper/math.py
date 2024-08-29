# This function checks if a given integer value is a prime number.
# It returns True if the number is prime and False otherwise.
# Note: The function currently does not handle cases for numbers less than 2 correctly.
def is_prime(val):
    is_prime = False if val==2 else True
    for x in range(2, val):
        if val%x==0:
            is_prime = False
            break

    return is_prime
