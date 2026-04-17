# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = []
        node = root
        def f(node):        
            if not node:
                return
            n.append(node.val)
            f(node.left)
            f(node.right)

        f(root)
        n.sort()
        return n[k-1]