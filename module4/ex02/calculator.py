#!/usr/bin/env python3

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")

print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
if second != 0:
    print(f"{first} / {second} = {first // second}")
else:
    print("Number cannot be divided by zero.")
print(f"{first} * {second} = {first * second}")
