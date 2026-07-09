#!/usr/bin/env python3

""" filter() needs function that returns true or false
filter(lambda item: item[1] == "red")
dupont_dict.items() = pairs
item[0] = name
item [1] = hair color """

def find_the_redheads(family_dict):
    red_dict = dict(filter(lambda i: "red" in i[1], family_dict.items()))
    return(list(red_dict.keys()))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))