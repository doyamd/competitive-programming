"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level = []
        d = defaultdict(list)
        def traverse(node,count):
            if not node:
                return None
            d[count].append(node)
            traverse(node.left,count + 1)
            traverse(node.right,count + 1)
        traverse(root,0)
        for i in range(len(d)):
            arr = d[i]
            for a in range(len(arr)-1):
                    arr[a].next = arr[a+1]
            arr[-1].next = None
        return root