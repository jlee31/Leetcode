# ============================================================
# TREES
# ============================================================
# When to use BFS:
#   - level-by-level processing
#   - shortest path / min depth
#   - "rightmost node per level", zigzag
#
# When to use DFS:
#   - height, diameter, max path sum
#   - subtree comparisons
#   - most other tree problems
#   - pre/in/post order traversal


# ── NODE DEFINITION ─────────────────────────────────────────

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ── BFS (LEVEL ORDER) ───────────────────────────────────────
# Key trick: snapshot len(queue) to process exactly one level per loop

from collections import deque

def bfs(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):   # process current level only
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


# ── DFS TEMPLATES ───────────────────────────────────────────

# Pre-order: root → left → right  (use for: serialize tree, copy tree)
def preorder(node):
    if not node:
        return
    print(node.val)      # process BEFORE children
    preorder(node.left)
    preorder(node.right)

# In-order: left → root → right  (use for: BST → sorted array)
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)      # process BETWEEN children
    inorder(node.right)

# Post-order: left → right → root  (use for: delete tree, compute subtree info)
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)      # process AFTER children

# DFS returning a value (most common pattern for mediums)
# — get info from children, combine, return to parent
def dfs(node):
    if not node:
        return 0           # base case: return identity value

    left = dfs(node.left)    # info from left subtree
    right = dfs(node.right)  # info from right subtree

    # combine left + right to compute something
    # update global result if needed

    return 1 + max(left, right)   # pass info UP to parent


# ── DFS WITH GLOBAL STATE ───────────────────────────────────
# Use when you need to track something across the whole tree
# (e.g. diameter, max path sum)

class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right)  # update global max
            return 1 + max(left, right)

        dfs(root)
        return self.res


# ── BST PROPERTIES ──────────────────────────────────────────
# Left subtree values < node < right subtree values
# In-order traversal of BST = sorted array ← KEY FACT

# Search in BST — O(log n) average
def search_bst(root, target):
    if not root:
        return None
    if root.val == target:
        return root
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

# Kth smallest in BST — in-order traversal, count to k
def kth_smallest(root, k):
    res = [0]
    count = [0]

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        count[0] += 1
        if count[0] == k:
            res[0] = node.val
        inorder(node.right)

    inorder(root)
    return res[0]


# ── COMMON PATTERNS ─────────────────────────────────────────

# Height of tree
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

# Check if tree is balanced (no subtree differs in height by > 1)
def is_balanced(node):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1   # signal unbalanced
        return 1 + max(left, right)
    return check(node) != -1

# Lowest Common Ancestor
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root   # p and q are on different sides
    return left or right
