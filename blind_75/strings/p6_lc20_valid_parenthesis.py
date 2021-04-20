class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")":"(", "]":"[", "}":"{" }

        if len(s)%2 != 0:
            return False
        
        for paren in s:
            if paren in lookup.values():
                stack.append(paren)
            elif stack and lookup[paren] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
        


sol = Solution()
#s = "()[]{}"

s2 = "([)]"

s3 = "{[]}"

print(f'false: {sol.isValid(s2)}')
print(f'true: {sol.isValid(s3)}')
















'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

https://leetcode.com/problems/valid-parentheses/



First attempt with some priority queue nonsense: 

priority = list(s)
        
        # create a dictionary to store the priority of each character
        dictionary = {priority[i] : i for i in range(len(priority))}
        
        #for char in range(s):
         #   if dictionary[char] < 

        return dictionary





'''