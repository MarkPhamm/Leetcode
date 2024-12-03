class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = [[] for _ in range(m)]
        if n*m < len(original) or n*m > len(original):
            return []
        index = 0
        count = 0
        for number in original:
            if count == n:
                index +=1
                count = 0
            ans[index].append(number)
            count+=1
        return ans

