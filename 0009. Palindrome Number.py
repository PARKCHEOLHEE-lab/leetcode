class Solution:
    """
        https://leetcode.com/problems/palindrome-number/
        
        Given an integer x, return true if x is a palindrome, and false otherwise.
    """
    def isPalindrome(self, x: int) -> bool:
        string_x_list = list(str(x))
        joined_string_x_list = "".join(string_x_list)
        
        reversed_string_x_list = list(reversed(string_x_list))
        joined_reversed_string_x_list = "".join(reversed_string_x_list)
        
        is_palindrome = joined_string_x_list == joined_reversed_string_x_list 
        
        return is_palindrome
    
    
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))