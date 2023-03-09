# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = defaultdict(list)

        def createLevel(root, depth):
            if not root:
                return

            level[depth].append(root.val)

            createLevel(root.left, depth + 1)
            createLevel(root.right, depth + 1)

        
        createLevel(root, 0)
        ans = [values[-1] for values in level.values()]
        return ans