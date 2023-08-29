class RomanNumerals:
    """Roman numerals colletion"""
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    
    IV = 4
    IX = 9
    XL = 40
    XC = 90
    CD = 400
    CM = 900
    

class Solution:
    """
    https://leetcode.com/problems/roman-to-integer/

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
    
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. 
    However, the numeral for four is not IIII. Instead, the number four is written as IV. 
    Because the one is before the five we subtract it making four. 
    The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.
    """

    roman_numerals = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }
    
    def romanToInt(self, s: str) -> int:
        
        total_integer = 0
        
        ri = 0
        while ri < len(s):
            curr_roman = s[ri]
            next_roman = s[(ri + 1) % len(s)] if ri != len(s) - 1 else ""
            roman_combination = getattr(RomanNumerals, curr_roman + next_roman, lambda: None)
            
            integer = getattr(RomanNumerals, curr_roman)
            
            if isinstance(roman_combination, int):
                total_integer += roman_combination
                ri += 2
                
            else:
                total_integer += integer
                ri += 1
        
        return total_integer

    def romanToInt2(self, s: str) -> int:
        
        integer = 0

        si = 0
        while si < len(s):
            
            curr_s = s[si]
            next_s = s[(si + 1) % len(s)]
            if si == len(s) - 1:
                next_s = ""

            merged_s = curr_s + next_s
            
            roman_to_integer = self.roman_numerals.get(merged_s)
            if roman_to_integer is None:
                roman_to_integer = self.roman_numerals.get(curr_s)
                si += 1

            else:
                si += 2

            integer += roman_to_integer
        
        return integer