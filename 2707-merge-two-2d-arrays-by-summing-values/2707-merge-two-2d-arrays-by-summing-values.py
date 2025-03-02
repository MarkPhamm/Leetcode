class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        def hashmap_sol(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
            # TC: O(N log(N))
            # SC: O()
            hash = {}
            ans = []
            for i, j in nums1:
                hash[i] = j
            
            for i,j in nums2:
                hash[i] = hash.get(i, 0) + j

            for i,j in hash.items():
                ans.append([i,j])
            
            print(ans)
            return sorted(ans)

        def two_pointer(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
            ans = []
            i, j = 0,0
            while i < len(nums1) and j < len(nums2):
                if nums1[i][0] < nums2[j][0]:
                    ans.append(nums1[i])
                    i+=1
                elif nums1[i][0] > nums2[j][0]:
                    ans.append(nums2[j])
                    j+=1
                else:
                    ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                    i+=1
                    j+=1
                
            ans.extend(nums1[i:])
            ans.extend(nums2[j:])
            
            return ans


        return two_pointer(self, nums1, nums2)