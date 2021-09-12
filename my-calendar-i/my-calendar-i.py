class MyCalendar:

    def __init__(self):
        #self.minTime = float("inf")
        #self.maxTime = float("-inf")
        self.calendar = []
    
    

    def book(self, start: int, end: int) -> bool:
        #self.minTime = min(self.minTime, start)
        #self.maxTime = max(self.maxTime, end)
        #print (self.calendar)
        if len(self.calendar) == 0:
            self.calendar.append((start, end))
        else:
            for event in self.calendar:
                # overlap
                if  event[0] <= start < event[1] or event[0] < end < event[1]:
                    return False    
                # spanning
                elif start <= event[0] and end >= event[1]:
                    return False    
            self.calendar.append((start, end))
        return True
                
'''

["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
    
----------------------------------------
                                 47----50
                        33---41                            
              25-----32
         19---25       
 3-8
   8-13
   
'''       

                

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)