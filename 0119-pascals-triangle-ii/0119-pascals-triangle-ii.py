class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Step 1: Define F: F(i,j) = row i column j
        # Step 2: Base case: F(i, 0) = F(i, i) = 1 with every i (on the edges and from the top)
        # Step 3: Recursive relation: F(i, j): = F(i -1, j - 1) + F(i - 1, j) 
        # Step 4: Implementation

        # Helper recursive function
        # i: row, j: column
        @lru_cache(None)
        def F(i,j):
            if j == 0 or i == j:
                return 1
            return F(i-1,j-1) + F(i-1,j)
        
        # Creating the index
        ans = []
        for j in range(rowIndex+1):
            ans.append(F(rowIndex,j))
        return ans
        

        

            
        