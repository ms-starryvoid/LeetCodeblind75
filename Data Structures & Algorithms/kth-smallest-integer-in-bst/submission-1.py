# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        stack=[]
        l=root
        count=0
        while stack or l:
            while l:
               stack.append(l)
               l=l.left 
            
            mi=stack.pop()
            count+=1
            if count==k:
                return mi.val
            l=mi.right
        return mi.val
        


        