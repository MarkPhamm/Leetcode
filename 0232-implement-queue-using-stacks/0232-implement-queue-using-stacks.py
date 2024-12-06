class MyQueue:

    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.size +=1

    def pop(self) -> int:
        first = self.arr[0]
        self.arr = self.arr[1:]
        self.size -=1
        return first

    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()