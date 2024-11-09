class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convert_to_base_ten(s: str) -> int:
            base_ten = 0
            base = 0
            for i in s[::-1]:
                base_ten += pow(2,base)*int(i)
                base+=1
            return base_ten
        
        sum = convert_to_base_ten(a) + convert_to_base_ten(b)

        def convert_to_binary(n):
            if n == 0:
                return "0"
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary
            
        return convert_to_binary(sum)

        