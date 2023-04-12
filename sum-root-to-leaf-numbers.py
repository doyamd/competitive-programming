# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        res = 0
        def dfs(node, num):
            nonlocal ans
            if not node:
                return 
            if not node.left and not node.right:
                ans.append(num+str(node.val))
            dfs(node.left, (num + str(node.val)))
            dfs(node.right, (num + str(node.val)))
        dfs(root, "")
        for i in ans:
            res += int(i)
        return res