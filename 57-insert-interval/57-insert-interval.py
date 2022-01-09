class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                merged.append(interval)
            elif interval[0] > newInterval[1]:
                merged.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        merged.append(newInterval)
        return merged
                
'''
T: O(N)
S: O(N)

intervals = [[1,3],[6,9]], newInterval = [2,5]


1--3---6---9--
  2--5  
  
Reference:  https://leetcode.com/problems/insert-interval/discuss/844549/Python-Super-Short-Simple-and-Clean-Solution-99-faster

'''