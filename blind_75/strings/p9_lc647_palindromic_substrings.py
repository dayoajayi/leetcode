class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result +=1
                l-=1
                r+=1

            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result +=1
                l-=1
                r+=1
        return result

sol = Solution()
s = "aaa"
print(sol.countSubstrings(s))

'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different 
substrings even they consist of same characters.

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

https://leetcode.com/problems/palindromic-substrings/
'''
