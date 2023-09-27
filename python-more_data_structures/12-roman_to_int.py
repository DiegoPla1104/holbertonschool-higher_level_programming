#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                    "D": 500, "M": 1000}
    number = 0

    for a in range(len(roman_string)):
        if roman_number.get(roman_string[a], 0) == 0:
            return (0)

        if (a != (len(roman_string) - 1) and
                roman_number[roman_string[a]] <
                roman_number[roman_string[a + 1]]):
            number += roman_number[roman_string[a]] * -1

        else:
            number += roman_number[roman_string[a]]
    return (number)
