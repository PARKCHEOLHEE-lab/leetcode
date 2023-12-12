class Solution:
    """
        https://leetcode.com/problems/valid-parentheses/
        
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
    """
    def isValid(self, s: str) -> bool:
        is_valid = False
        if len(s) == 0:
            return is_valid
    
        brackets = "()"
        middle_brackets = "{}"
        large_brackets = "[]"
        
        while (
            brackets in s 
            or middle_brackets in s 
            or large_brackets in s
        ):
            s = s.replace(brackets, "")
            s = s.replace(middle_brackets, "")
            s = s.replace(large_brackets, "")
            
            is_valid = len(s) == 0
            
        return is_valid
    
    def isValid2(self, s: str) -> bool:
        brackets_collection = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        
        reversed_brackets_collection = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        
        stack = []
        for bracket in s:
            if bracket in brackets_collection:
                stack.append(bracket)
                
            elif len(stack) == 0 or stack.pop() != reversed_brackets_collection[bracket]:
                return False
            
        return len(stack) == 0

    def isValid3(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        
        stack = []

        for bracket in s:
            
            # opening bracket
            if bracket in brackets:
                stack.append(bracket)
                continue
            
            if len(stack) == 0:
                return False

            # closing bracket
            if bracket != brackets[stack.pop()]:
                return False

        return len(stack) == 0

    
print(Solution().isValid2("(([]){})"), True)
print(Solution().isValid2("(}{)"), False)
print(Solution().isValid2("({{{{}}}))"), False)
print(Solution().isValid2("(){}}{"), False)
print(Solution().isValid2("){"), False)
print(Solution().isValid2("))))(((("), False)
print(Solution().isValid2("([)]"), False)
print(Solution().isValid2("({[]})"), True)
print(Solution().isValid2("()"), True)
print(Solution().isValid2("()[]{}"), True)
print(Solution().isValid2("(]"), False)
print(Solution().isValid2("({}[])"), True)