# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        cur = head
        prev = dummy
        index = 1
        while cur:
            n = cur.next
            if index%2 == 0:
                if index == 2:
                    cur.next = prev
                    prev.next = n
                    prep_swap = prev
                    head = cur
                    cur = n
                    index +=1
                else:
                    print(cur.val)
                    cur.next = prev
                    prep_swap.next = cur
                    prep_swap = prev
                    prev.next = n
                    cur = n
                    index +=1
            else:
                cur = n
                prev = prev.next
                index +=1
        
        return head

        

        