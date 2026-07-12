class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op=0
        clo=0
        res=[]
        def dfs(s,op,clo):
            if op<clo or op>n:
                return
            if clo==n and op ==n:
                #check valid string if yes append to res
                res.append(s)
                return
            dfs(s+'(',op+1,clo)
            dfs(s+')',op,clo+1)
        dfs("(",1,0)
        return res
            