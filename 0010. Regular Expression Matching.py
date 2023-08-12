from functools import lru_cache 

class Solution:
    """https://leetcode.com/problems/regular-expression-matching/submissions/

        Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

        '.' Matches any single character.​​​​
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).

        Example 1:
            Input: s = "aa", p = "a"
            Output: false
            Explanation: "a" does not match the entire string "aa".

        Example 2:
            Input: s = "aa", p = "a*"
            Output: true
            Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

        Example 3:
            Input: s = "ab", p = ".*"
            Output: true
            Explanation: ".*" means "zero or more (*) of any character (.)".

        Constraints:
            1 <= s.length <= 20
            1 <= p.length <= 20
            s contains only lowercase English letters.
            p contains only lowercase English letters, '.', and '*'.
            It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
    """
    
    DOT = "."
    ASTERISK = "*"

    @lru_cache
    def isMatch(self, text: str, pattern: str) -> bool:
        if len(pattern) == 0:
            return len(text) == 0
        
        first_match = len(text) >= 1 and (text[0] == pattern[0] or pattern[0] == self.DOT)
        
        if len(pattern) >= 2 and pattern[1] == self.ASTERISK:
            is_match_1 = first_match and self.isMatch(text[1:], pattern)
            is_match_2 = self.isMatch(text, pattern[2:])

            return is_match_1 or is_match_2
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
    
    
solution = Solution()
assert solution.isMatch(text="aaaaa", pattern="a*") is True
assert solution.isMatch(text="aab", pattern="c*a*b") is True
assert solution.isMatch(text="misssssissippi", pattern="mis*is*ip*.") is True
assert solution.isMatch(text="aaa", pattern="ab*ac*a") is True
assert solution.isMatch(text="miaissippi", pattern="mis*is*ip*.") is False
assert solution.isMatch(text="asdfff", pattern="asdf*") is True
assert solution.isMatch(text="abcd", pattern="d*") is False

assert solution.isMatch(text="aabb", pattern="a..b") is True
assert solution.isMatch(text="aab", pattern="cca*b") is False
assert solution.isMatch(text="aaa", pattern="aaaa") is False
assert solution.isMatch(text="aa", pattern="a") is False