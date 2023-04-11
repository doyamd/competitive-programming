# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        arr = ""
        def dfs(node):
            nonlocal arr
            if not node:
                return
            arr += "("    
            arr += str(node.val)
            if not node.left and node.right:
                arr += "()"
            
            dfs(node.left)

            dfs(node.right)
            arr += ")"
        dfs(root)
        return arr[1:-1]