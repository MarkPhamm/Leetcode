class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.array = []
        

    def next(self, val: int) -> float:
        self.array.append(val)
        if len(self.array) < self.size:
            return sum(self.array)/len(self.array)
        else:
            return sum(self.array[-self.size:])/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)