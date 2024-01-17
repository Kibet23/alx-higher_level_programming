#!/usr/bin/python3
def fizzbuzz():
    """
    print numbers from 1 to 100 with Fizz for multiples of 3,
    Buzz for multiples of 5 and FizzBuzz for multiples of both

    Returns:
        None
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
