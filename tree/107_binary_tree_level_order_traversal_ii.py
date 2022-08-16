# Given the root of a binary tree, return the bottom-up level order traversal
# of its nodes' values. (i.e., from left to right, level by level from leaf to root).


import collections


class TreeNode:
    """ Definition for a binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            lev_len = len(q)
            level = []
            for _ in range(lev_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res[::-1]
