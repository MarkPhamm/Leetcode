class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_base_ten = 0
        base = 0

        for i in a[::-1]:
            a_base_ten += pow(2,base)*int(i)
            base+=1
        
        b_base_ten = 0
        base = 0  

        for i in b[::-1]:
            b_base_ten += pow(2,base)*int(i)
            base+=1

        sum = a_base_ten + b_base_ten

        def convert_to_binary(n):
            if n == 0:
                return "0"
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary
            
        return convert_to_binary(sum)

        