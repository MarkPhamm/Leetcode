class ProductOfNumbers:
    # Idea: 
    # Eg: nums = [3,0,2,5,4]
    # self.p = [3,3,6,30,120]
   
    # Step 1: Create prefix product self.p, if num = 0 then treat it as 1
    # Step 2: Keep track the index of the last 0 self.last_zero 
    # Get product k last number = 
        # if not include 0 (k< len(p) - last_zero): return p[-1] / p[len(p)-k-1]
        # else: return 0 
    # edge cases: k = len(s)

    def __init__(self):
        self.p = [] # keep track of prefix product p
        self.last_zero = -1 # keep track of the last 0
        
    def add(self, num: int) -> None:
        # construct prefix product p
        if not self.p: # if the prefix arr is empty
            if num != 0: 
                self.p.append(num) # append num
            else:
                self.last_zero = 0
                self.p.append(1)
        else:
            if num != 0: 
                self.p.append(self.p[-1]*num) 
            else: 
                self.last_zero = len(self.p) # update the last_zero
                self.p.append(self.p[-1]) # add the last number, treat the 0 as 1

    def getProduct(self, k: int) -> int:
        start = len(self.p) - k
        if start <= self.last_zero:
            return 0
        else:
            if len(self.p) == k:
                return self.p[-1]
            else:
                return int(self.p[-1] / self.p[start-1])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)