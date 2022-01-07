class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        output = [intervals[0]]
        
        for start, end in intervals:
            prevEndTime = output[-1][1]
            if start <= prevEndTime:
                output[-1][1] = max(prevEndTime, end)
            else:
                output.append([start,end])
        return output
    
        
'''
        intervals = sorted(intervals)
        output = [intervals[0]]

        for start, end in intervals:
            prevEndtime = output[-1][1]  # ==> 
            if start <= prevEndtime:
                output[-1][1] = max(prevEndtime, end)
            else:
                output.append([start,end])
        print(output)
        return output
        
        intervals: [[1,3],[2,6],[8,10],[15,18]]
        output.  : [[1,6],[8,10],[15,18]]
        
'''