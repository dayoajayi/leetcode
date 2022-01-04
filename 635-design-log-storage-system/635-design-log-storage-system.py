class LogSystem:

    def __init__(self):
        self.logs = []
        self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}
        

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append([timestamp, id])

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.g[granularity]
        s,e = start[:idx], end[:idx]
        
        print (self.logs)
        return [i for time, i in self.logs if s <= time[:idx] <= e]

#     4  7         19    
# 2017:01:01:23:59:59
# self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

        
# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)

'''
Time: O(N)
Space: O(N)
'''