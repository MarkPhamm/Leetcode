class TwoSum:

    def __init__(self):
        self.arr = []


    def add(self, number: int) -> None:
        self.arr.append(number)
        return None

    def find(self, value: int) -> bool:
        hashmap = {}
        for num in self.arr:
            if num in hashmap:
                return True 
                break 
            else:
                hashmap[value - num] = num
        return False

# [1,3,5]
# [3:1]
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)