#!/usr/bin/python3
def print_last_digit(number):
	"""Print the last digit of a number and return"""
	ldigit = abs(number) % 10
	print(ldigit, end="")
	return (ldigit)
