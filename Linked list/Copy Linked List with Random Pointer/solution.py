"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create a mapping of original nodes to their copy nodes.
        node_map = {}


        # First pass: create all nodes and store them in a hashmap
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

        # Step 2: Assign next and random pointers for the copied nodes
        current = head
        while current:
            if current.next:
                node_map[current].next = node_map[current.next]
            if current.random:
                node_map[current].random = node_map[current.random]
            current = current.next


        # Return the head of the copied list
        return node_map[head]
