#!/usr/bin/env python
 

def fib(end_number):
    num1 = 0
    num2 = 1
    sum = 0
    while(num2 < end_number):
        sum = num1 + num2
        print('{0}, {1}'.format(num1, num2))
        num1 = sum
        num2 = num1 + num2

fib(1000)


