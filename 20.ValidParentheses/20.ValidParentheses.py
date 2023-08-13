class Solution:
    def isValid(self, s: str) -> bool:
# Assumptions:
#open brackets must be closed by the same type of brackets
#open Brackets must be closed in the correct order
# we r going to use LIFO Stack
        stack = []
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for bracket in s :
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
        return len(stack) == 0