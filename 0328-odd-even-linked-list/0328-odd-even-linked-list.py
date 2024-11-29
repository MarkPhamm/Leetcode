# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(None, head.next)
        odd = head
        even = head.next

        while odd.next and odd.next.next and even.next and even.next.next:
            n_odd = odd.next.next
            n_even = even.next.next
            odd.next = n_odd
            even.next = n_even
            odd = n_odd
            even = n_even
        if odd.next and odd.next.next:
            n_odd = odd.next.next
            odd.next = n_odd
            odd = n_odd
            even.next = None
        elif even.next and even.next.next:
            n_even = even.next.next
            even.next = n_even
            even = n_even
            odd.next = None

        odd.next = dummy.next
        dummy.next = None
        return head