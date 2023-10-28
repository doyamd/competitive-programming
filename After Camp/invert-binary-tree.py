# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traveres(node):
            if not node:
                return
            temp_right = None
            temp_left = None
            if node.right:
                temp_right = node.right
            if node.left:
                temp_left = node.left
            node.right = temp_left
            node.left = temp_right
            traveres(node.left)
            traveres(node.right)
            
        traveres(root)
        return root
