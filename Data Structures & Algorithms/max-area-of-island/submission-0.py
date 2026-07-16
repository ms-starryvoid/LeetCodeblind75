class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxA=0
        rows=len(grid)
        cols=len(grid[0])
        
        visited=set()
        dire=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            area=1
            q=collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in dire:
                    r,c=row+dr,col+dc
                    if(r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
                        area+=1
            return area

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]==1:
                    area=bfs(r,c)
                    maxA=max(area,maxA)
        return maxA
                    