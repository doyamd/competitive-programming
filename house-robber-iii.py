# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        d = {}

        def dp(node):
            if not node:
                return 0
            if node not in d:
                left,right = node.val,node.val
                
                if node.left:
                    left += dp(node.left.left) + dp(node.left.right)
                if node.right:
                    right += dp(node.right.left) + dp(node.right.right)

                comp1 = left + right - node.val    
                comp2 = dp(node.left) + dp(node.right)
                
                d[node] = max(comp1,comp2)
            return d[node]
             

    

        return dp(root)