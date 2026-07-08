#!/usr/bin/env python3

# filter() needs function that returns true or false
# filter(lambda item: item[1] == "red")
# dupont_dict.items() = pairs
# item[0] = name
# item [1] = hair color
def find_the_redheads(dupont_dict):
	return(list(filter(lambda item: item[0] == "red", dupont_dict.items())))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))