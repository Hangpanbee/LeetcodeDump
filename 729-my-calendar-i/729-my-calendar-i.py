class MyCalendar:

    def __init__(self):
        self.bookedCalendar = []

    def book(self, start: int, end: int) -> bool:
        """
        [20,29,36,42,45,50]
        [ s, e, s, e, s, e]
        
        """
        si = bisect.bisect_right(self.bookedCalendar, start)
        ei = bisect.bisect_left(self.bookedCalendar, end)
        if ei == si and si%2==0:
            self.bookedCalendar.insert(si, start)
            self.bookedCalendar.insert(ei+1, end)
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)