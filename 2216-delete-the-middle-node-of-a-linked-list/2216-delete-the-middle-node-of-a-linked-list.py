# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count +=1

        middle = ceil((count+1)/2)

        index = 1
        dummy = ListNode(None, head)
        cur = dummy.next
        prev = dummy

        while index != middle:
            cur = cur.next
            prev = prev.next
            index +=1
        
        n = cur.next
        prev.next = n
        cur.next = None
        return dummy.next
        