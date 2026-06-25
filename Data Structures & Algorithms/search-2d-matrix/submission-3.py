class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        down = len(matrix) - 1

        while top <= down:
            mid = (top + down) // 2
            if matrix[mid][0] > target:
                down = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        l = 0
        r = len(matrix[0]) - 1
        mid = (top + down) // 2

        while l <= r:
            mid2 = (l + r) // 2
            if matrix[mid][mid2] > target:
                r = mid2 - 1
            elif matrix[mid][mid2] < target:
                l = mid2 + 1
            else:
                return True
        return False