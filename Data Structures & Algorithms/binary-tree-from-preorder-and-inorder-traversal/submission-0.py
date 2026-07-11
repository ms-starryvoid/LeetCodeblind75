# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_indx=0
        iorder_map={val:i for i,val in enumerate(inorder)}
        def build(left,right):
            nonlocal pre_indx
            if left>right:
                return None
            root_val=preorder[pre_indx]
            pre_indx+=1

            mid=iorder_map[root_val]
            root=TreeNode(root_val)
            root.left=build(left,mid-1)
            root.right=build(mid+1,right)
            return root
        return build(0,len(inorder)-1)
