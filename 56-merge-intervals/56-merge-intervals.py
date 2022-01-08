class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        # intervals = [[1,3],[2,6],[8,10],[15,18]]
        
        '''
            1--3
              2----6
                     8--10    15--18
            ----------------------------------------------            
        '''
        
        output = [intervals[0]]
        
        for start, end in intervals:
            prevEndTime = output[-1][1]
            if start <= prevEndTime:
                output[-1][1] = max(prevEndTime, end)
            else:
                output.append([start, end])
        return output
    
'''
T: O(NlogN)
S: O(N)

'''