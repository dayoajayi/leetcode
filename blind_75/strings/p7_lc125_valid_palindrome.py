class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_text= ''.join(filter(str.isalnum, s))
        return str.lower(stripped_text[::]) == str.lower(stripped_text[::-1])
        




'''
Given a string s, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

https://leetcode.com/problems/valid-palindrome/

'''

sol = Solution()
#s = "A man, a plan, a canal: Panama"
s = "race a car"
print(sol.isPalindrome(s))