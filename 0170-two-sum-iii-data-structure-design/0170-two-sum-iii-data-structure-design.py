class TwoSum:

    def __init__(self):
        self.list = []
        

    def add(self, number: int) -> None:
        self.list.append(number)

    def find(self, value: int) -> bool:
        hashmap = {}
        for n in self.list:
            if n in hashmap:
                return True
            hashmap[value-n] = n
        return False
            
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)