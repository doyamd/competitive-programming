# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        g_child = 0
        def grand(node):
            nonlocal g_child
            if node.left and node.left.left:
                g_child += node.left.left.val
            if node.left and node.left.right:
                g_child += node.left.right.val
            if node.right and node.right.right:
                g_child += node.right.right.val
            if node.right and node.right.left:
                g_child += node.right.left.val
            
        def traverse(nod):
            if not nod:
                return 
            if nod.val % 2 == 0:
                grand(nod)
            traverse(nod.left)
            traverse(nod.right)
        traverse(root)
        return g_child