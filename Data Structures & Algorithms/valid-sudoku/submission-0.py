class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        box=defaultdict(set)
        for i in range(9):
            for j in range(9):
                l=board[i][j]
                b=(i//3,j//3)
                if l == ".":
                    continue
                elif l in rows[i] or l in cols[j] or l in box[b]:
                    return False
                else:
                    rows[i].add(l)
                    cols[j].add(l)
                    box[b].add(l)
        return True