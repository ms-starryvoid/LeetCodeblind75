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
        stack=[root]
        l=root
        count=0
        while stack and count<k:
            if l:
               stack.append(l)
               l=l.left 
            else:
                mi=stack.pop()
                count+=1
                if mi.right:
                    l=mi.right
        return mi.val
        


        