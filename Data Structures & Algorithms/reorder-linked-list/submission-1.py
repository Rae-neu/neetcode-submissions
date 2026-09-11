# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        cur2 = slow.next
        slow.next = None

        pre = None
        cur = cur2
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        cur1 = head
        cur2 = pre

        while cur2:
            nxt1 = cur1.next
            nxt2 = cur2.next

            cur1.next = cur2
            cur2.next = nxt1

            cur1 = nxt1
            cur2 = nxt2
        

