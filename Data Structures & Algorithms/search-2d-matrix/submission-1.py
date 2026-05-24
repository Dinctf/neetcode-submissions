class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS=len(matrix)
        COLS=len(matrix[0])
        low=0
        high=ROWS-1
        while low<=high:
            row=(low+high)//2
            if target>matrix[row][-1]:
                low=row+1
            elif target<matrix[row][0]:
                high=row-1
            else:
                break
        if not low<=high:
            return False
        row=(low+high)//2
        l=0
        r=COLS-1
        while l<=r:
            mid=(l+r)//2
            if target>matrix[row][mid]:
                l=mid+1
            elif target<matrix[row][mid]:
                r=mid-1
            else:
                return True
        return False

        