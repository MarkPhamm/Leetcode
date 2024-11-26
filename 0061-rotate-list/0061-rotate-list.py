# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 0
        cur = head
        while cur:
            length +=1
            cur = cur.next

        effective_k = k%length
        print(effective_k)

        for i in range(effective_k):
            dummy = ListNode(None, head)
            prev = dummy
            cur = dummy.next
            while cur.next:
                cur = cur.next
                prev = prev.next
            print(cur)
            prev.next = None
            cur.next = dummy.next
            head = cur

        return head
            
        