class MyCalendarThree:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> int:
        si = bisect.insort_right(self.calendar, (start, 1))
        ei = bisect.insort_left(self.calendar, (end, -1))
        
        
        maxBooking = 0
        currBooking = 0
        for i, booking in enumerate(self.calendar):
            currBooking += booking[1]
            maxBooking = max(maxBooking, currBooking)
            
        return maxBooking
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)