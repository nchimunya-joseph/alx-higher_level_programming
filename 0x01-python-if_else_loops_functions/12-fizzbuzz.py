#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end=" ")
        if i % 5 == 0:
            print("Buzz", end=" ")
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        print(i, end=" ")
    print("")
