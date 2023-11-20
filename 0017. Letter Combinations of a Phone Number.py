import itertools
from typing import List

class Solution:
    
    """
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

        Example 1:
            Input: digits = "23"
            Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        Example 2:
            Input: digits = ""
            Output: []

        Example 3:
            Input: digits = "2"
            Output: ["a","b","c"]
    """
    
    DIGITS_MAP = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def cartesianProduct(self, *all_lists):
        product = [[]]
        for each_list in all_lists:
            
            each_product = []
            for p in product:
                for each_element in each_list:
                    each_product.append(p + [each_element])

            product = each_product
            
        return product

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digits_list = [self.DIGITS_MAP[digit] for digit in digits if digit in self.DIGITS_MAP]
        letter_combinations = self.cartesianProduct(*digits_list)

        return [''.join(combination) for combination in letter_combinations]

    def letterCombinationsWithItertools(self, digits: str) -> List[str]:
        letter_combinations = list(
            map("".join, itertools.product(*[self.DIGITS_MAP[digit] for digit in digits]))
        ) if len(digits) != 0 else []

        return letter_combinations
    

if __name__ == "__main__":
    Solution().letterCombinations(digits="234")