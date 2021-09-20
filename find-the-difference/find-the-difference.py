class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        result = ""
        
        
        diff = (t_counter - s_counter)
        
        for d in diff.elements():
            result += d
            
        return result