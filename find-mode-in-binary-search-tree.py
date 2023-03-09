# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cont = Counter()
        ans = []
        def traverse(root):
            if not root:
                return 
            cont[root.val] += 1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        sorted_d = sorted(cont.items(), key=lambda x:x[1])
        max_count = sorted_d[-1][-1]
        for val,count in sorted_d:
            if count == max_count:
                ans.append(val)
        return ans