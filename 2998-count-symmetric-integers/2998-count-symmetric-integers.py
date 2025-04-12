class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            str_i = str(i)
            if len(str_i) % 2 == 0:
                middle = int(len(str_i) / 2 )
                left_sum = 0
                right_sum = 0
                for i in range(middle):
                    left_sum += int(str_i[i])
                    right_sum += int(str_i[middle+i])
                if left_sum == right_sum:
                    ans +=1
        return ans