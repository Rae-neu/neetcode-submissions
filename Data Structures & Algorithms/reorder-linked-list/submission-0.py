# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        cur2 = slow.next
        slow.next = None

        cur = cur2
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        cur1 = head
        while pre:
            next1 = cur1.next
            next2 = pre.next

            cur1.next = pre
            pre.next = next1

            cur1 = next1
            pre = next2








        

        
