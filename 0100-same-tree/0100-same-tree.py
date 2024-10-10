# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return p.left==q.left or p.left==q.right
        if p==None and q==None: return 1
        if p==None or q==None or p.val!=q.val:return 0
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    ###
        