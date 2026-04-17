class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                l, r = 0, len(matrix[i]) - 1
                while l <= r:
                    c = (l + r) // 2
                    if target > matrix[i][c]:
                        l = c + 1
                    elif target < matrix[i][c]:
                        r = c - 1
                    else:
                        return True
        return False