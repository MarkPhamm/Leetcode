class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = (n+1)*n/2
        total_m = m*int(n/m)*(int(n/m)+1)/2
        return int(total_sum - total_m*2)