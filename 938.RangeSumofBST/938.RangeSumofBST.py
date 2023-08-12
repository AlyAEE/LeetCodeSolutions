import typing
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: [TreeNode], low: int, high: int) -> int:
# we can solve this problem using recursive depth first search
        sum = 0
        def dfs(node):
            if not node:
                return 
            if low <= node.val <= high:
                nonlocal sum
                sum += node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return sum

# Using iterative DFS with Stack                              
        # stack = [(root, root.val)]
        # sum = 0
        # while stack:
        #     node, val = stack.pop()
        #     if low <= val <= high:
        #         sum += val
        #     if node.left:
        #         stack.append((node.left, node.left.val))
        #     if node.right:
        #         stack.append((node.right, node.right.val))
        # return sum

# Using Breadth First Search
        
        # d = collections.deque([(root, root.val)])
        # a = 0
        # while d:
        #     node, val = d.popleft()
        #     if low <= val <= high:
        #         a += val
        #     if not ( node.left or node.right):
        #         continue
        #     if node.left:
        #         d.append((node.left, node.left.val))
        #     if node.right:
        #         d.append((node.right, node.right.val))
        # return a

   




