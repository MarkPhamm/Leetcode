class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = {}
        for char in arr:
            hashmap[char] = hashmap.get(char,0) + 1
        
        ans = []
        for key, value in hashmap.items():
            if value == 1:
                ans.append(key)
        if k-1 >= len(ans):
            return ""
        else:
            return ans[k-1]