# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        node = root
        d = defaultdict(int)
        res = []
        def dp(node):
            if not node:
                return ' '
            sub = str(node.val) + '.'+dp(node.left)+'.'+dp(node.right)
            d[sub] += 1
            if d[sub] == 2:
                res.append(node)
            return sub

        dp(node)
        return res