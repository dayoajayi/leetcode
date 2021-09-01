class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        output = [intervals[0]]
        
        for start, end in intervals:
            prevEndtime = output[-1][1]
            if start <= prevEndtime:
                output[-1][1] = max(prevEndtime, end)
            else:
                output.append([start,end])
        print(output)
        return output
        
        
#   1----6    
#--------------------------------        
#   1--3
#     2--6
#           8--10
#                  15--18
        


