# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_elem = []
        for l in lists:
            cur = l
            while cur:
                all_elem.append(cur.val)
                cur = cur.next
        all_elem = sorted(all_elem)
        
        dummy = ListNode()
        current = dummy

        for num in all_elem:
            current.next = ListNode(num)
            current = current.next

        head = dummy.next

        return head
        