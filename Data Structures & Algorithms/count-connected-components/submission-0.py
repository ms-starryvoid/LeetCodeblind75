class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if px==py:
            return False
        if self.rank[px]>self.rank[py]:
            self.parent[py]=px
        elif self.rank[px]<self.rank[py]:
            self.parent[px]=py
        else:
            self.parent[py]=px
            self.rank[px]+=1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf=UnionFind(n)
        count=n
        for e,v in edges:
            if uf.union(e,v):
                count-=1
        return count
        