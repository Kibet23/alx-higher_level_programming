#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f'{10} is positive')
elif number == 0:
    print(f'{0} is zero')
else:
    print(f'{-10} is negative')
