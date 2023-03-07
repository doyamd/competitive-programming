# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        unsorted = []
        def traverse(node):
            if not node:
                return unsorted
            traverse(node.left)
            unsorted.append(node.val)
            traverse(node.right)
            return unsorted
        traverse(root)
        
        sorted_lis = sorted(unsorted)
        if unsorted == sorted_lis and len(set(sorted_lis)) == len(unsorted):
            return True
        else:
            return False