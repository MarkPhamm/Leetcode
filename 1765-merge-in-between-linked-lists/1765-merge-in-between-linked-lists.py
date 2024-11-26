# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left_index = 0
        right_index = 0

        dummy = ListNode(None, list1)
        left_node = dummy.next
        right_node = dummy.next
        
        while left_index < a-1:
            left_node = left_node.next
            left_index +=1

        while right_index < b+1:
            right_node = right_node.next
            right_index +=1

        
        cur = list2
        left_node.next = cur

        while cur.next:
            cur = cur.next
        
        cur.next = right_node
        return dummy.next