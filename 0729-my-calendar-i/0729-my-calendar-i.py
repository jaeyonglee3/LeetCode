class MyCalendar:

    def __init__(self):
        # an array of intervals representing events
        # we will maintain this such that events are sorted in ascending order by start time
        self.events = []

        # (6, 7)
        # (4, 5)

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.events:
            if startTime < e and s < endTime:
                return False
        
        self.events.append((startTime, endTime))
        return True
                    
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)