class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        # Helper recursive function
        # i: row, j: column
        @lru_cache(None)
        def F(i,j):
            if j == 0 or i == j:
                return 1
            return F(i-1,j-1) + F(i-1,j)
        
        ans = []
        for j in range(rowIndex+1):
            ans.append(F(rowIndex,j))
        
        return ans
        

        

            
        