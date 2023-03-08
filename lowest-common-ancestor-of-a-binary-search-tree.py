# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def isFound(root,p,q):
            if not root:
                return False
            if root == q or root == p:
                return True
            return isFound(root.left,p,q) or isFound(root.right,p,q)
        def search(root,p,q):
            if not root:
                return root
            if (root == p or root == q) and isFound(root,p,q):
                ans = root
                return ans
            if isFound(root.right,p,q) and isFound(root.left,p,q):
                ans = root
                return ans
            if not isFound(root.right,p,q) and isFound(root.left,p,q):
                return search(root.left,p,q)
            if isFound(root.right,p,q) and not isFound(root.left,p,q):
                return search(root.right,p,q)
        return search(root,p,q)