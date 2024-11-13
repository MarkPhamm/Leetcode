class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Start and end with 1
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        else: 
            base = [[1], [1,1]]
            while True:
                middle = []
                for i in range(len(base[-1])-1):
                    middle.append(base[-1][i]+ base[-1][i+1])
                base.append([1] + middle + [1])
                if len(base) == numRows:
                    return base


        