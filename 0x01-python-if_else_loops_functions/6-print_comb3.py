#!/usr/bin/python3
for num in range(10):
    for num2 in range(num + 1, 10):
        if num != num2:
            print("{:d}{:d}".format(num, num2), end=", " if num < 8 or num2 < 9 else "\n")
