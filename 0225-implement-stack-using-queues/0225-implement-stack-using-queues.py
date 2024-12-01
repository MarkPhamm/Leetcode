class MyStack:

    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.size +=1

    def pop(self) -> int:
        top = self.arr[-1]
        self.arr.pop()
        self.size -=1
        return top
        

    def top(self) -> int:
        return self.arr[-1]

    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()