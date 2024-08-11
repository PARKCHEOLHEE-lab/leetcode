class Solution:
    """
        https://leetcode.com/problems/valid-anagram/
        https://en.wikipedia.org/wiki/Anagram

        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

        Example 1:
            Input: s = "anagram", t = "nagaram"
            Output: true

        Example 2:
            Input: s = "rat", t = "car"
            Output: false

        Constraints:
            1 <= s.length, t.length <= 5 * 104
            s and t consist of lowercase English letters.
    """
    
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        for s_spell in s:
            if s_spell not in s_counter:
                s_counter[s_spell] = 0
            s_counter[s_spell] += 1

        t_counter = {}
        for t_spell in t:
            if t_spell not in t_counter:
                t_counter[t_spell] = 0
            t_counter[t_spell] += 1
        
        return s_counter == t_counter