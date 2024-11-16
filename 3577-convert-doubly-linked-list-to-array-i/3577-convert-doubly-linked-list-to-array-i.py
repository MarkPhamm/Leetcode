"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        while root.prev is not None:
            root = root.prev
        
        arr = []
        while root:
            arr.append(root.val)
            root = root.next
        
        return arr

            
        