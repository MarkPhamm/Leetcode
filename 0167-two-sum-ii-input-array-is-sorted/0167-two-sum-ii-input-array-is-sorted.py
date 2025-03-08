class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def two_pointer(self, numbers: List[int], target: int) -> List[int]:
            # TC: O(n)
            # SC: O(1)
            i = 0
            j = len(numbers)-1
            while numbers[i] + numbers[j] != target:
                if numbers[i] + numbers[j] > target:
                    j-=1
                else:
                    i+=1
            return [i+1,j+1]

        def hashmap(self, numbers: List[int], target: int) -> List[int]:
            hashmap = {}

            for index, value in enumerate(numbers):
                print(index, value)
                if target - value in hashmap:
                    return [hashmap[target - value]+1, index+1]
                if value not in hashmap:
                    hashmap[value] = index
        
        return hashmap(self, numbers, target)