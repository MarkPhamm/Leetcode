# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = set()  # Use a set for efficient lookup
        cur = head
        while cur:
            if cur in check:
                return True
            check.add(cur)
            cur = cur.next  # Move to the next node
        return False  # No cycle found