class Logger:

    def __init__(self):
        self.cache = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.cache:
            self.cache[message] = timestamp + 10 
            return True
        else:
            if timestamp >= self.cache[message]:
                self.cache[message] = timestamp+10
                return True
            else:
                return False
                
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)