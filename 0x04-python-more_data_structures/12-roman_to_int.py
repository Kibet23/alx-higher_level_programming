#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000}
    result = 0
    prev_val = 0

    for numeral in reversed(roman_string):
        curr_val = roman_numerals.get(numeral, 0)

        if curr_val < prev_val:
            result -= curr_value

        else:
            result += curr_val

        prev_val = curr_val

        return (result)
