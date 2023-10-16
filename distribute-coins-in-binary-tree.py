# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            temp = (node.val+l+r)-1
            count += abs(temp)
            return temp
        node = root
        dfs(node)
        return count