class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = arr.copy()
        arr_sorted.sort()
        skip = 0
        hashmap = {}
        for i in range(len(arr_sorted)):
            if arr_sorted[i] not in hashmap:
                hashmap[arr_sorted[i]] = i + 1 - skip
            else:
                skip+=1
        
        ans = []
        for num in arr:
            ans.append(hashmap[num])

        return ans

