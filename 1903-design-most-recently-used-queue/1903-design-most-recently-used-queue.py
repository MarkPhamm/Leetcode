class MRUQueue:

    def __init__(self, n: int):
        self.array = []
        for i in range(1,n+1):
            self.array.append(i)
    def fetch(self, k: int) -> int:
        num = self.array[k-1]
        self.array.pop(k-1)
        self.array.append(num)
        return num
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)