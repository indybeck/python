The numeric system represented by Roman numerals originated in ancient Rome. Numbers in this system are represented by combinations of letters from the Latin alphabet. Roman numerals, as we use them today, are based on seven symbols:

I:1; V:5; X:10; L:50; C:100; D:500; M: 1,000

You have a string s that represents a number written as a Roman numeral. If the string s is a correctly written Roman numeral, return this number as an integer. If s isn't a correctly written Roman numeral, return -1.

For this challenge, assume that there is no restriction on the maximum number that can be written in Roman numerals.

Example

For s = "MMXV", the output should be
integerValueOfRomanNumeral(s) = 2015;

For s = "XLX", the output should be
integerValueOfRomanNumeral(s) = -1.

XL is a valid Roman numeral representing 40, but XLX is not valid.

Input/Output

[time limit] 4000ms (py)
[input] string s

A string s consisting of characters I, V, X, L, C, D, M.

Guaranteed constraints:
1 ≤ s.length ≤ 100.

[output] integer

The integer value of the given Roman numeral, or -1 if the input doesn't contain a correct Roman numeral.