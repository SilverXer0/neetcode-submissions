class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                val = int(board[row][col]) - 1
                mask = 1 << val
                if (mask & rows[row]) or (mask & cols[col]) or (mask & squares[(row // 3) * 3 + (col // 3)]):
                    return False

                rows[row] |= mask
                cols[col] |= mask
                squares[(row // 3) * 3 + (col // 3)] |= mask

        return True


                
        