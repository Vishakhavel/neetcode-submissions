class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 arrays of 9 hashsets in each
        cols = []
        rows = []
        boxes = []

        for i in range(9):
            cols.append(set())
            rows.append(set())
            boxes.append(set())

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if(cur == '.'):
                    continue
                boardIndex = 3*(i//3) + j//3

                if(cur in rows[i] or cur in cols[j] or cur in boxes[boardIndex]):
                    return False
                else:
                    rows[i].add(cur)
                    cols[j].add(cur)
                    boxes[boardIndex].add(cur)
        
        return True