class Logger:
    """
    message may or may not be unique
    condition:
        in (< 10 i for i in (forever))
            -> message - Uuid -> print
    
    """
    def __init__(self):
        self.ts = {}       

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.ts:
            if abs(self.ts[message] - timestamp) >= 10:
                self.ts[message] = timestamp
                return True
            else:
                return False     
        else:
            self.ts[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)