class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        count = 0
        for i in arr:
            if i+1 in s:
                count +=1
        return count
        