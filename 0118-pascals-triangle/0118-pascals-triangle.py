class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [0 for _ in range(row_num+1)]
            row[0], row[-1] = 1,1
            
            for j in range(1, len(row)-1):
                prev_row = row_num - 1
                row[j] = triangle[prev_row][j - 1] + triangle[prev_row][j]
            
            triangle.append(row)
        return triangle

        