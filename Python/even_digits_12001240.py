#!/usr/bin/env python3

# Question:
# Write a Python program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on
# a single line.
#
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Solution:

def has_all_even_digits(n):
    for d in n:
        if (int(d) % 2):
            return False
    return True

result = []
for i in range(1000, 3001):
    n = str(i)
    if has_all_even_digits(n):
        result.append(n)
print(','.join(result))
