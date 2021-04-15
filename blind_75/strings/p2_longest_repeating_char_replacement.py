class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        maxCount = 0
        N = len(s)
        start = end = 0
        charCount = [0] * 26
        
        while end < N:
            # Add to the character count in our sliding window:
            charCount[ord(s[end]) - ord('A')] += 1
            maxCount = max(maxCount, charCount[ord(s[end]) - ord('A')])

            while (end - start - maxCount + 1) > k:
                charCount[ord(s[end]) - ord('A')] -= 1
                start += 1
            maxlen = max(maxlen, end-start+1)
            end += 1

        return maxlen


sol = Solution()

s, k = "ABAB", 2

print(sol.characterReplacement(s,k))
