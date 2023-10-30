# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        ans = []
        node = root
        if not root:
            return []
        def dfs(node,parent,is_left):
            if not node:
                return
            # print(node.val)
            l,r = node.left, node.right
            if node.val in delete:
                if node.left:
                    if node.left.val not in delete:
                        ans.append(node.left)
                if node.right:
                    if node.right.val not in delete:
                        ans.append(node.right)
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            dfs(l,node,True)
            dfs(r,node,False)
            del node
        if node.val not in delete:
            ans.append(node)
            dfs(node,-1,False)
        else:
            if node.left and node.left.val not in delete:
                ans.append(node.left)
            dfs(node.left,node,True)
            if node.right and node.right.val not in delete:
                ans.append(node.right)
            dfs(node.right,node,False)

        return ans
        