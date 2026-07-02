class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        lo, hi = 0, rows - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if target > matrix[mid][-1]:
                lo = mid + 1
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                break

        # lo being the top of the matrix, hi being the bottom of the matrix
        # this is saying that if the top is "past" the bottom i.e. no more rows to search
        if not (lo <= hi): 
            return False

        row = (lo + hi) // 2
        l, h = 0, cols - 1
        while l <= h:
            mid = (l + h) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                h = mid - 1
            else:
                return True

        return False