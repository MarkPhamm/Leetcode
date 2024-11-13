class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        base = [[1], [1,1]]
        while True:
            mid = []
            for i in range (len(base[-1])-1):
                mid.append(base[-1][i] + base[-1][i+1])
            
            base.append([1] + mid +[1])
            if len(base[-1]) == rowIndex+1:
                return base[-1]
            

        