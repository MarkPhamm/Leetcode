# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        if head is not None and head.next is not None:
            dummyeven = ListNode(None, head.next)
        else: 
            return head
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

        print(even.val, odd.val)
        odd.next = dummyeven.next
        dummyeven.next = None
        return dummy.next