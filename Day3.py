# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        while l1 != None and l2 != None:            
            if l1.val <= l2.val:
                new_node = ListNode(l1.val)  
                l1 = l1.next            
            else:
                new_node = ListNode(l2.val)            
                l2 = l2.next
                
        # while l1 != None:            
        #     new_node = ListNode(l1.val)
        #     l1 = l1.next
            
        # while l2 != None:            
        #     new_node = ListNode(l2.val)                                 
        #     l2 = l2.next
            
    return new_node

    ########################################################

    class Solution:
    def decodeString(self, s: str) -> str:
      
# i dont know how to tackle this problem

