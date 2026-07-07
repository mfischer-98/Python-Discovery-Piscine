#!/usr/bin/env python3

my_list = [2, 8, 9, 48, 8, 22, -12, 2]
#new_list = [n + 2 for n in my_list]
new_list = []

print(my_list)
for number in my_list:
    number += 2
    new_list.append(number)

print(new_list)