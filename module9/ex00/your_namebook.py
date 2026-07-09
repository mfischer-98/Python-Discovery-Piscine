#!/usr/bin/env python3

""" 	to access each item in dictionary = keys and values
	in this loop key, value = (jean, valjean)
	to access only keys: for name in name_dict """

def array_of_names(name_dict):
	name_list = []
	for key, value in name_dict.items():
		name_list.append(key.capitalize() + " " + value.capitalize())
	return name_list

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))