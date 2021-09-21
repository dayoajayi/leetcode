class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rem, res, a, b = 0, "", list(a), list(b)
        
        while a or b:
            if a: rem += int(a.pop())
            if b: rem += int(b.pop())
            res = str(rem % 2) + res
            rem = rem // 2
            
        return str(rem) + res if rem == 1 else res
