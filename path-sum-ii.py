# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        node = root
        queue = [(node.val,[node.val],node)]
        visited = set()
        ans = []
        # print(node.val)

        while queue:
            sums, arr, node  = queue.pop(0)
            if not node.right and not node.left and sums == targetSum:
                if node not in visited:
                    visited.add(node)
                    ans.append(arr)
            if node.left:
                queue.append((sums + node.left.val,arr+[node.left.val],node.left))
            if node.right:
                queue.append((sums + node.right.val,arr+[node.right.val],node.right))
        return ans