#!/usr/bin/env python3

my_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []

print(my_list)
for number in my_list:
    if (number > 5):
        number += 2
        new_list.append(number)

print(set(new_list))