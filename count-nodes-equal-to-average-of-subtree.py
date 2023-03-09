# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def getNum(root):
            nonlocal count
            if not root:
                return (0,0)

            left = getNum(root.left)
            right = getNum(root.right)

            sums = left[0] + right[0] + root.val
            depth = left[1] + right[1] + 1
            avg = sums // depth

            if avg == root.val:
                count += 1
            return (sums,depth)
        getNum(root)
        return count