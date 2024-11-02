from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        def recur(node):
            if not node:
                return '#'
            return str(node.val) + "," + recur(node.left) + "," + recur(node.right)

        return recur(root)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        def  recur(nodes: List[str]) -> Optional[TreeNode]:
            if nodes[0] == '#':
                nodes.pop(0)
                return None

            root = TreeNode(int(nodes[0]))
            nodes.pop(0)    # Remove the value we just used
            root.left = recur(nodes)
            root.right = recur(nodes)
            return root
        
        node_list = data.split(",")
        return recur(node_list)
