class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        i = 0
        curr_row = row1
        for i in range(row2-row1+1):
            j = col1
            while j <= col2:
                s += self.matrix[curr_row][j]
                j += 1
            curr_row += 1

        return s