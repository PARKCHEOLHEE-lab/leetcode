class Solution:
    """
        https://leetcode.com/problems/reverse-integer/

        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    """
    
    RANGE_MAX = 2 ** 31

    def reverse(self, x: int) -> int:
    
        x_string_reversed = str(x)[::-1]
        x_string_replaced = x_string_reversed.replace("-", "")
        x_integer_reversed = int(x_string_replaced) if x > 0 else -int(x_string_replaced)

        if -self.RANGE_MAX <= x_integer_reversed <= self.RANGE_MAX - 1:
            return x_integer_reversed

        return 0