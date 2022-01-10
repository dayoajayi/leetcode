class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max(end for start, end in events)
        days = 0
        event_id =  0
        num_events_attended = 0
        min_heap = []
                
        for day in range(1, total_days + 1):
            while event_id < len(events) and events[event_id][0] == day:
                heappush(min_heap, events[event_id][1])
                event_id += 1
                
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
                
            if min_heap: 
                heappop(min_heap)
                num_events_attended += 1
        
        return num_events_attended
            