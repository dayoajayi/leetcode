class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        roomsUsed = []
        
        heapq.heappush(roomsUsed,intervals[0][1])
        
        for i in range(1, len(intervals)):
            if roomsUsed[0] <= intervals[i][0]:
                heapq.heappop(roomsUsed)
            heapq.heappush(roomsUsed, intervals[i][1])
        
        return len(roomsUsed)
    
'''
T: O(NLogN)
S: O(N)
'''