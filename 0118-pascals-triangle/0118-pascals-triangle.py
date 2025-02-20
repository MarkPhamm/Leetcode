class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Step 1: Define F: F(i,j) = row i column j
        # Step 2: Base case: F(i, 0) = F(i, i) = 1 with every i (on the edges and from the top)
        # Step 3: Recursive relation: F(i, j): = F(i -1, j - 1) + F(i - 1, j) 
        # Step 4: Implementation

        # F(3,3) = F(2,2) + F(2,3) = F(1,1) + F(1,2) + F(1,2) + F(1,3)
        # = F(1,1) + 2F(1,2) + F(1,3)
        # = F(0,0) + F(0,1) + 2(F(0,1) + F(0,2)) + F(0,3)
        # ^n Exponential 
        # TLO: TC: (O(x^n)) without memorization, O(n^2) with memorization
        # SC: O(N)

        # cache memorization, every (i,j) we calculate only once -> only need to calculate all i,j pair
        memo = {}

        # Helper recursive function
        def F(i: int,j: int):
            if (i,j) in memo: # check the memo:
                return memo[i,j]
            
            if j == 0 or j == i:
                return 1
            return_value = F(i-1, j-1) + F(i-1, j)
            memo[i,j] = return_value
            return return_value

        ans = []
        for i in range(numRows):
            ans.append([])
            for j in range(i+1):
                ans[-1].append(F(i,j))
        
        print(memo)
        return ans
