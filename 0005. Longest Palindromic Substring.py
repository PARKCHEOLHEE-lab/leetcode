class Solution:
    """
        https://leetcode.com/problems/longest-palindromic-substring/description/
        
        Given a string s, return the longest palindromic substring in s.
        
        Reference: https://leetcode.com/problems/longest-palindromic-substring/solutions/3834196/2-solutions-with-explanation-expand-around-center-dp-python/
    """
    
    def longestPalindrome(self, s: str) -> str:
        # Runtime: 7272 ms
        
        if len(s) == 1:
            return s
        
        longest_palindrome = ""
        for si in range(len(s) - 1):
            sub_palindrome = s[si]
            
            for other_s in s[si + 1:]:
                sub_palindrome += other_s
                
                if sub_palindrome == reversed(sub_palindrome) and len(longest_palindrome) < len(sub_palindrome):
                    longest_palindrome = sub_palindrome
        
        return longest_palindrome if len(longest_palindrome) > 0 else s[0]
        
    def longestPalindrome(self, s: str) -> str:
        # Runtime: 387 ms

        def _expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left + 1 : right]

        longest_palindrome = ""
        for i in range(len(s)):            
            palindrome1 = _expand_around_center(i, i)
            palindrome2 = _expand_around_center(i, i + 1)

            current_longest = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2

            if len(current_longest) > len(longest_palindrome):
                longest_palindrome = current_longest

        return longest_palindrome

print(Solution().longestPalindrome("asddsa"))
