class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]
:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None
    
#         self.next = next
#         self.val = val
#     def __init__(self, val=0, next=None):
# Definition for singly-linked list.
# class ListNode:
    def merge(self, linked1,linked2):
        ans = ListNode(0)
        curr1 = linked1
        curr2 = linked2
        currAns = ans
            
        while curr1 and curr2:
            if curr1.val >= curr2.val:
                currAns.next = curr2
                curr2 = curr2.next
            else:
                currAns.next = curr1
                curr1 = curr1.next
            currAns = currAns.next
        if curr1: