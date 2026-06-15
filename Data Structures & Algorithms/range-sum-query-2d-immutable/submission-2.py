class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_sum = matrix
        for row in range(len(self.matrix)):
            acc = 0
            for col in range(len(self.matrix[row])):
                self.prefix_sum[row][col] += acc
                acc = self.prefix_sum[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2+1):
            if col1 > 0:
                res += self.prefix_sum[row][col2] - self.prefix_sum[row][col1-1]
            else:
                res += self.prefix_sum[row][col2]
        return res