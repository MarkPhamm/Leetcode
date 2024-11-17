class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash_map = {}
        for index,groupSize in enumerate(groupSizes):
            if groupSize in hash_map:
                hash_map[groupSize].append(index)
            else:
                hash_map[groupSize] = []
                hash_map[groupSize].append(index)

        ans = []
        for key, val in hash_map.items():
            if len(val) == key:
                ans.append(val)
            else:
                while len(val) != 0:
                    ans.append(val[:key])
                    val = val[key:]
        
        return ans