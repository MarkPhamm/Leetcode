class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = 0
        max_zeros = 0
        current_ones = 0
        current_zeros = 0

        for i in s:
            if i == "1":
                current_ones +=1 
                max_ones = max(current_ones, max_ones)
                current_zeros = 0
            if i == "0":
                current_zeros +=1 
                max_zeros = max(current_zeros, max_zeros)
                current_ones = 0
        
        return max_ones > max_zeros



        