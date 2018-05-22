"""
Quiz 6
Question 1
Write a function, fizzbuzz that prints the numbers from 1 to 100.
For each multiple of 3, print “Fizz” instead of the number.
For each multiple of 5, print “Buzz” instead of the number.
For numbers which are multiples of both 3 and 5, print “FizzBuzz” instead of the number.
"""


def fizzbuzz():
    for n in range(1, 101):
        if n % 5 == 0 and n % 3 == 0:
            print(n, "FizzBuzz")
        elif n % 3 == 0:
            print(n, "Fizz")
        elif n % 5 == 0:
            print(n, "Buzz")
        else:
            print(n)


fizzbuzz()
