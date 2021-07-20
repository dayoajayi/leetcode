        # intervals = [[0,30],[5,10],[15,20]]
        # intervals = [[7,10],[2,4]]
        
        # 0--5--10--15--20--25--30
        # |----------------------|
        #    |---|
        #            |---|
        
        

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True