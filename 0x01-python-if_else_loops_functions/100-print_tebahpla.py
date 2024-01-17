#!/usr/bin/python3

for alpha in range(90, 64, -1):
    print("{:c}".format(alpha + 32 if alpha % 2 == 0 else alpha), end="")
