# Definition for singly-linked list.
# class ListNode
#     def __init__(self, val=0, next=None)
#         self.val = val
#         self.next = next
class Solution
    def deleteDuplicates(self, head Optional[ListNode]) - Optional[ListNode]
        if not head
            return head
        c = head.next
        p = head
        while c
            if c.val != p.val
                p.next = c
                p = c
            c = c.next
        p.next = c
        return head