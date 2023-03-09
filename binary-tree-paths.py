# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        def backtrack(node,arr):
            if not node:
                return 
            if not node.right and not node.left:
                if arr != '':
                    arr = arr + '->' + str(node.val)
                else:
                    arr = arr + str(node.val)
                path.append(arr)
                return
            
            if arr != '':
                arr = arr + '->' + str(node.val)
            else:
                arr = arr + str(node.val)
            backtrack(node.left,arr)
            backtrack(node.right,arr)
        backtrack(root,'')
        return path