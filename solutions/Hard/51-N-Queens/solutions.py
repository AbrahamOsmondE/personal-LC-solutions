class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."]*n for _ in range(n)]
        
        diagonals,anti_diagonals,cols = set(),set(),set()
        
        def submit_board(board):
            res = []
            for row in board:
                res.append("".join(row))
            
            return res
        
        def backtrack(row):
            if row == n:
                ans.append(submit_board(board))
            
            for col in range(n):
                anti_diag = row + col
                diag = row - col
                
                if col in cols or anti_diag in anti_diagonals or diag in diagonals:
                    continue
                
                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)
                board[row][col] = "Q"
                
                backtrack(row+1)
                
                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)
                board[row][col] = "."
                
        backtrack(0)
        return ans
        