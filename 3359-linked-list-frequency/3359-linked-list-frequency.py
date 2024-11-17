# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        counter = {}
        cur = head
        while cur:
            counter[cur.val] = counter.get(cur.val, 0)+1
            cur = cur.next
        
        print(counter)
        head = ListNode(list(counter.values())[0])
        cur = head
        for key, val in list(counter.items())[1:]:
            cur.next = ListNode(val)
            cur = cur.next

        cur.next = None
        return head

