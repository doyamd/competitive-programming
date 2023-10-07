# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d = defaultdict(list)
        d[root.val] = [-1]
        node = root
        heap=[(node.val,node)]
        fq = False
        fp = False
        while heap:
            
            val, node = heappop(heap)
            # print(val)
            if node == q:
                fq = True
            if node == p:
                fp = True
            if fq and fp:
                break
            if node and node.left:
                d[node.left].append(node)
                d[node.left].extend(d[node])
                heappush(heap,(node.left.val,node.left))
            if node and node.right:
                d[node.right].append(node)
                d[node.right].extend(d[node])
                heappush(heap,(node.right.val,node.right))
        set_p = set(d[p])
        set_q = set(d[q])
        # print(set_q,set_p)
        arr = d[p]
        if q in set_p:
            return q
        if p in set_q:
            return p
        for i in arr:
            if i in set_q:
                return i
        return 0