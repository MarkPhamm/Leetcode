class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        hashmap_s1 = {}
        hashmap_s2 = {}
        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] not in hashmap_s1:
                    hashmap_s1[s1[i]] = s2[i]
                else:
                    return False
                if s2[i] not in hashmap_s2:
                    hashmap_s2[s2[i]] = s1[i]
                else:
                    return False
        print(hashmap_s1)
        return (hashmap_s1 == hashmap_s2) and len(hashmap_s1) <= 2
        