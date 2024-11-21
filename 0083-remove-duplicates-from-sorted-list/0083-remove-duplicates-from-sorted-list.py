# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        c = head
        p = dummy
        while c:
            if c.val == p.val:
                n = c.next
                p.next = n
                c.next = None
                c = n
            else:
                c = c.next
                p = p.next
        return dummy.next



        