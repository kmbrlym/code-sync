"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(n):
            if not n:
                return
            if n in oldToNew:
                return oldToNew[n]
            new_n = Node(n.val)
            oldToNew[n] = new_n
            for i in n.neighbors:
                new_n.neighbors.append(dfs(i))
            return new_n
        return dfs(node)