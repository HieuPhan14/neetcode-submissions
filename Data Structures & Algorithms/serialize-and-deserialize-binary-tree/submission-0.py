# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return 'null'

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + ',' + right
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = deque(data.split(','))
        return self.build(values)

    def build(self, values):
        val = values.popleft()
        if val == 'null':
            return None
        node = TreeNode(int(val))
        node.left = self.build(values)
        node.right = self.build(values)
        return node

        
