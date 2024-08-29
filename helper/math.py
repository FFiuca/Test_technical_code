def is_prime(val):
    is_prime = False if val==2 else True
    for x in range(2, val):
        if val%x==0:
            is_prime = False
            break

    return is_prime
