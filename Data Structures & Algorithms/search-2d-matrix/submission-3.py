class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                left = 0
                right = len(matrix[m]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if target < matrix[m][mid]:
                        right = mid - 1
                    elif target > matrix[m][mid]:
                        left = mid + 1
                    else:
                        return True
                return False

        return False

