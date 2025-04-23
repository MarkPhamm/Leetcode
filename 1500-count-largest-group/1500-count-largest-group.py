class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digit(n):
            sum = 0
            while n != 0:
                sum += n % 10
                n //= 10
            return sum
        
        max_length = 0
        count = 0
        hashmap = {}
        for i in range(1, n+1):
            key = sum_digit(i)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(i)
            cur_length = len(hashmap[key])
            if cur_length > max_length:
                max_length = cur_length
                count = 1
            elif cur_length == max_length:
                count +=1
        print(hashmap)
        return count