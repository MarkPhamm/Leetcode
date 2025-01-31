class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = [0]
        for num in range(1, n+1):
            prefix_sum.append(num+prefix_sum[-1])

        for i in range(1,n+1):
            if (prefix_sum[-1]+i)/2 == prefix_sum[i]:
                return i

        return -1
        
        