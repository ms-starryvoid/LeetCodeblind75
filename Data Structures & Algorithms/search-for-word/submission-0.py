class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        s=""
        visited=[]
        def dfs(i,j,count):
            if [i,j] in visited:
                return
            
            if count==len(word):
                return True
            if i== len(board) or j== len(board[0])or i < 0 or j < 0 :
                return

            if board[i][j]==word[count]:
                visited.append([i,j])
                count+=1
                found=(dfs(i,j+1,count) or
                dfs(i+1,j,count) or
                dfs(i-1,j,count) or
                dfs(i,j-1,count))
                visited.remove([i,j])
                return found
            else:
                return 
                
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False

           

        