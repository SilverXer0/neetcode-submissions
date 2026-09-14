class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                char = board[row][col]
                if char == '.':
                    continue
                if char in rows[row] or char in cols[col] or char in squares[(row//3, col//3)]:
                    return False
                
                rows[row].add(char)
                cols[col].add(char)
                squares[(row//3, col//3)].add(char)

        return True        
