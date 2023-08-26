class Solution:
    """
        https://leetcode.com/problems/integer-to-roman/
    
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given an integer, convert it to a roman numeral.        

        Example 1:
            Input: num = 3
            Output: "III"
            Explanation: 3 is represented as 3 ones.

        Example 2:
            Input: num = 58
            Output: "LVIII"
            Explanation: L = 50, V = 5, III = 3.

        Example 3:
            Input: num = 1994
            Output: "MCMXCIV"
            Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
            
        Constraints:
            1 <= num <= 3999
    """
    
    roman_numerals = {
            1: "I",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
            1000: "M",
        }

    chipers_string = "0"
    chipers_number = 10
    
    def intToRoman(self, num: int) -> str:
        num_string = str(num)
        num_string_chipers = range(len(num_string) - 1, -1, -1)
        
        roman = ""
        for chipers, num_str in zip(num_string_chipers, num_string):
            if int(num_str) == 0:
                continue

            integer = int(num_str + self.chipers_string * chipers)      
            integer_to_roman = self.roman_numerals.get(integer)

            if integer_to_roman is None:
                integer_str = str(integer)
                multiplier = len(str(integer)) - 1
                integer_to_roman = self.roman_numerals.get(self.chipers_number ** multiplier) * int(integer_str[0])

            roman += integer_to_roman
        
        return roman  