class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_list = list(str(n))
        sum = 0
        product = 1
        for i in n_list:
            sum += int(i)
            product = product * int(i)
            
        return product-sum
    
        