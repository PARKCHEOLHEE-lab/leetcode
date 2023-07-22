class Solution:
    """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

        Given a string s, find the length of the longest substring without repeating characters.
    """
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s_length = len(s)
        if s_length in (0, 1):
            return s_length

        substrings = []
        for si in range(s_length - 1):
            substring = s[si]

            for other_s in s[si + 1:]:

                if other_s in substring:
                    break

                substring += other_s
        
            substrings.append(substring)

        longest_substring, *_ = sorted(substrings, key=lambda s: len(s), reverse=True)

        return len(longest_substring)