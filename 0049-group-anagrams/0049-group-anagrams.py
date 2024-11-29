class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            key = ''.join(sorted(list(string)))
            print(key)
            if key  in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
        
        ans = []
        for key, val in hashmap.items():
            ans.append(val)
        
        return ans
        