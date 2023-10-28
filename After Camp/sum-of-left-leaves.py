# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        node = root
        def traverse(node,is_left):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right and is_left:
                ans += node.val
            traverse(node.left,True)
            traverse(node.right,False)
        traverse(node,False)
        return ans

