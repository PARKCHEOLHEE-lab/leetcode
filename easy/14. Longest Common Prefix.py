from typing import List

class Solution:
    """
        https://leetcode.com/problems/longest-common-prefix/
        
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        if len(strs) < 1:
            return common_prefix

        longest_string_length = len(sorted(strs, key=lambda s: len(s), reverse=True)[0])
        converted_strs = [s + " " * (longest_string_length - 1) for s in strs]
        
        si = 0
        while si < longest_string_length:
            checker = [string[si] for string in converted_strs if len(string) > 0]
            if len(set(checker)) == 1 and not (len(converted_strs) >= 2 and "" in (converted_strs)) and list(set(checker))[0] != " ":
                common_prefix += checker[0]
            else:
                break
            
            if len(checker) <= 1:
                break
            
            si += 1
        return common_prefix
    
    
# print(Solution().longestCommonPrefix(["c","c","c","c"]), "c")
# print(Solution().longestCommonPrefix(["flower","flower","flower","flower"]), "flower")
# print(Solution().longestCommonPrefix(["flower","flow","flight"]), "fl")
# print(Solution().longestCommonPrefix(["dog","racecar","car"]), "")
# print(Solution().longestCommonPrefix(["a"]), "a")
# print(Solution().longestCommonPrefix([""]), "")
# print(Solution().longestCommonPrefix(["","b"]), "")
# print(Solution().longestCommonPrefix(["ab", "a"]), "")