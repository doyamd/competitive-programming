# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = defaultdict(list)
        visited = set()
        ans = []
        def traverse(node,par):
            if not node:
                return
            d[node.val].append(par.val)
            if node.right:
                d[node.val].append(node.right.val)
                traverse(node.right,node)
            if node.left:
                d[node.val].append(node.left.val)
                traverse(node.left,node)
        if root.right:
            d[root.val].append(root.right.val)
            traverse(root.right,root)
        if root.left:
            d[root.val].append(root.left.val)
            traverse(root.left,root)
       
       
        queue = deque([target.val])
        count = -1
        while queue and count != k:
            count += 1
            for l in range(len(queue)):
                num =queue.popleft()
                if num not in visited:
                    visited.add(num)
                    if count == k:
                        ans.append(num)
                    for i in d[num]:
                        queue.append(i)
        return ans