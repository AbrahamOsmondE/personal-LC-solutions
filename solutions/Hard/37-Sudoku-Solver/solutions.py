                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)
                
                if backtrack(r,c+1):
                    return True
                
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_id].remove(num)
            return False
        backtrack(0,0)
        n = len(board)
        rows, cols, boxes = collections.defaultdict(set), collections.
defaultdict(set), collections.defaultdict(set)
        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                v = int(board[r][c])
                rows[r].add(v)
                cols[c].add(v)
                boxes[(r // 3) * 3 + c // 3].add(v)
        def is_valid(r, c, v):
            box_id = (r // 3) * 3 + c // 3
            return v not in rows[r] and v not in cols[c] and v not in boxes