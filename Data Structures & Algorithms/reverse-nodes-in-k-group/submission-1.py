# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next
                
            groupStart = groupPrev.next
            groupNext = kth.next

            cur = groupStart
            pre = groupNext

            while cur != groupNext:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            groupPrev.next = kth
            groupPrev = groupStart
        
        return dummy.next