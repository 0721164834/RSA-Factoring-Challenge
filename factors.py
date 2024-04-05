#!/usr/bin/env python3

import sys

def factorize(number):
    """
    Factorize a given number into two smaller numbers.
    """
    for p in range(2, number):
        if number % p == 0:
            q = number // p
            return p, q
    return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            for line in f:
                number = int(line.strip())
                p, q = factorize(number)
                if p is not None and q is not None:
                    print(f"{number} = {p} * {q}")
                else:
                    print(f"Unable to factorize {number} into two smaller numbers.")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Invalid input. Please provide a valid file containing natural numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
