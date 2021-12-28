class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        
        for paren in s:
            if paren in lookup.values():
                stack.append(paren)
            elif stack and lookup[paren] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []