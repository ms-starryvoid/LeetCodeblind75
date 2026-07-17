class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        row,col=len(grid),len(grid[0])
        q=deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append((r,c))
        dire=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            for dr,dc in dire:
                nr=r+dr
                nc=dc+c
                if (0<=nr<row) and (0<=nc<col) and grid[nr][nc]==2147483647:
                    grid[nr][nc]=grid[r][c]+1
                    q.append((nr,nc))