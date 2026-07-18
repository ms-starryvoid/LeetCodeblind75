class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        mins=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        dire=[(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh>0:
            for _ in range(len(q)):
                row,col=q.popleft()
                for r,c in dire:
                    dr=r+row
                    dc=c+col
                    if ((0<=dr<rows) and (0<=dc<cols)) and grid[dr][dc]==1:
                        grid[dr][dc]=2
                        fresh-=1
                        q.append((dr,dc))
            mins+=1
        if fresh>0:
            return -1
        return mins

