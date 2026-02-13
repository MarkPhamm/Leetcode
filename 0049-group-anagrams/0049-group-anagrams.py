class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for string in strs:
            str_sorted = sorted(string)
            common_key = tuple(str_sorted)
            
            lookup[common_key] = lookup.get(common_key, [])
            lookup[common_key].append(string)
        
        ans = []
        for v in lookup.values():
            ans.append(v)
        
        return ans 