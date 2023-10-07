# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        d = defaultdict(list)
        node = root
        heap = [(0,1,node)]
        visited = set()
        while heap:
            depth, val, node = heappop(heap)
            d[depth].append(val)
            if node and node.left:
                heappush(heap,(depth+1,val*2,node.left))
            if node and node.right:
                heappush(heap,(depth+1,(val*2)+1,node.right))
        for k, v in d.items():
            ans = max(ans,(v[-1]-v[0])+1)
        return ans