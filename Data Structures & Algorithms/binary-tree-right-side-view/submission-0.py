# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for each level
        # find the rightmost value in the bfs

        ret = []

        def bfs(root):
            if not root:
                return
            
            queue = deque([root])

            while queue:
                level_size = len(queue)  # number of nodes at this level
                
                for i in range(level_size):
                    node = queue.popleft()
                    print(node.val)  # process node

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                        
                    if i == level_size - 1:  
                        ret.append(node.val)

                print('end of level')
    
        bfs(root)
        return ret