# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self, l,r):
        if not(l or r): return 1
        if not(l and r): return 0
        return l.val==r.val and self.mirror(l.left,r.right) and self.mirror(l.right,r.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root.left,root.right) if root else 1
        