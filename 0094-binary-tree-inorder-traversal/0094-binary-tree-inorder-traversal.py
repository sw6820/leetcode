# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global r
        r=[]        
        def inorder(node):
            if node.left:inorder(node.left)                            
            r.append(node.val)
            if node.right:inorder(node.right)                
        if root: inorder(root)
        return r
            