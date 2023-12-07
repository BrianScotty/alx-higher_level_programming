#!/usr/bin/python3

def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    r_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_numbers = [r_data[x] for x in roman_string] + [0]
    roman_n = 0

    for i in range(len(r_numbers) - 1):
        if r_numbers[i] >= r_numbers[i+1]:
            roman_n += r_numbers[i]
        else:
            roman_n -= r_numbers[i]

    return roman_n
