# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def travers(node):
            if not node:
                return ans
            travers(node.left)    
            ans.append(node.val)
            travers(node.right)
            return ans
        return travers(root)