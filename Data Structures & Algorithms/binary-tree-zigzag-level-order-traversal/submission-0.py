# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        def bfs(node):
            if not node:
                return
            queue = deque([root])
            height = 1
        
            while queue:
                level = []
                level_size = len(queue)

                for i in range(level_size):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                        
                if height % 2 == 0:
                    ret.append(level[::-1])
                else:
                    ret.append(level)

                height += 1

        bfs(root)
        return ret