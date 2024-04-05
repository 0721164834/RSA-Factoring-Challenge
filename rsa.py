#!/usr/bin/env python3

def factorize(number):
    """
    Factorize a given number into two prime factors.
    """
    for p in range(2, number):
        if number % p == 0:
            q = number // p
            return p, q
    return None, None

def main():
    try:
        # Replace this with the actual RSA number you want to factorize
        n = int(input("Enter the RSA number to factorize: "))
        
        p, q = factorize(n)
        if p is not None and q is not None:
            print(f"Factorization of {n}:")
            print(f"{n} = {p} * {q}")
        else:
            print(f"Unable to factorize {n} into two prime numbers.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()

