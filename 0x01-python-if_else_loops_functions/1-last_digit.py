#!/usr/bin/python3
import sys
import random
number = random.randint(-10000, 10000)
sys.stdout.write('Last digit of {} is {}'.format(number, number % 10))
if number % 10 > 5:
    sys.stdout.write(' and is greater than 5')
elif number % 10 < 6 and number % 10 != 0:
    sys.stdout.write(' and is less than 6 and not 0')
else:
    sys.stdout.write(' and is 0')
sys.stdout.write('\n')
