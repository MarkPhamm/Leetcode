# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # TC: O(n)
        # SC: O(1)
        # Idea: 
        # Step 1: traverse both nodes and update cur value to the to the current value of the list until l1 or l2 end
        # Step 2: update the rest (or the larger node) into cur.next  
        
        # Step 1: traverse both nodes and update cur value to the to the current value of the list until l1 or l2 end
        dummy = cur = ListNode(None)
        while list1 != None and list2 != None:
            if list1.val <=  list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else: 
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next

        # Step 2: update the rest (or the larger node) into cur.next
        if list1 != None:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next

                

                
        