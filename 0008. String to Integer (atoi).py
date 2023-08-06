class Constants:
    
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    MINUS = "-"
    PLUS = "+"
    COMBINATION = ["++", "+-", "-+", "--"]

class Solution(Constants):
    """
        https://leetcode.com/problems/string-to-integer-atoi/
        
        Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

        The algorithm for myAtoi(string s) is as follows:

        Read in and ignore any leading whitespace.
        Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. 
        This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
        Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
        Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
        If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
        Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
        Return the integer as the final result.
        
        Note:
        Only the space character ' ' is considered a whitespace character.
        Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
        
        Constraints:
        0 <= s.length <= 200
        s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

    """

    def myAtoi(self, s: str) -> int:
        ascii_string_replaced_whitespace = s.lstrip()
        
        if len(ascii_string_replaced_whitespace) == 0:
            return 0

        sign = self.MINUS if ascii_string_replaced_whitespace[0] == self.MINUS else self.PLUS

        if ascii_string_replaced_whitespace[:2] in self.COMBINATION:
            return 0

        ascii_string_strip_sign = ascii_string_replaced_whitespace.lstrip(self.PLUS).lstrip(self.MINUS)

        result_ascii_string = ""
        for each_string in ascii_string_strip_sign:
            if not each_string.isdigit():
                break
            
            result_ascii_string += each_string

        if len(result_ascii_string) == 0:
            ascii_to_integer = 0

        else:
            ascii_to_integer = int(sign + result_ascii_string)
            if ascii_to_integer > self.MAX:
                ascii_to_integer = self.MAX
            elif ascii_to_integer < self.MIN:
                ascii_to_integer = self.MIN
        
        return ascii_to_integer