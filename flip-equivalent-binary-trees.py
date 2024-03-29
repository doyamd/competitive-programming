# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        node1 = root1
        node2 = root2
        
        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            if (n1 and not n2) or (not n1 and n2) or (n1.val != n2.val):
                return False
            return (dfs(n1.right,n2.right) and dfs(n1.left,n2.left)) or (dfs(n1.left,n2.right) and dfs(n1.right,n2.left))
        return dfs(node1,node2)