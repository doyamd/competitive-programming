# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)

        def createLevel(root, depth):
            if not root:
                return

            level[depth].append(root.val)

            createLevel(root.left, depth + 1)
            createLevel(root.right, depth + 1)

        
        createLevel(root, 0)
        return level.values()