class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes={}
        for r in range(9):
            for c in range(9):
                cell=board[r][c]
                if cell ==".":
                    continue
                box=(r//3,c//3)
                if box not in boxes:
                    boxes[box]=set()
                if cell in rows[r] or cell in cols[c] or cell in boxes[box]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[box].add(cell)
        return True

        