#!/usr/bin/env python3
 
first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))

mult = first * second
print(f"{first} x {second} = {mult}")

if mult < 0:
    print("The result is negative.")
elif mult > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
