# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = {}
        dummy = ListNode(None, head)
        cur = dummy.next
        while cur:
            counter[cur.val] = counter.get(cur.val,0)+1
            cur = cur.next
        
        to_delete = []
        for key, val in counter.items():
            if val >= 2:
                to_delete.append(key)
        
        slow = dummy
        
        while slow.next:
            if slow.next.val not in to_delete:
                slow = slow.next
        
            fast = slow.next
            while fast:
                if fast.val not in to_delete:
                    break
                fast = fast.next
            slow.next = fast
        return dummy.next
                    
        