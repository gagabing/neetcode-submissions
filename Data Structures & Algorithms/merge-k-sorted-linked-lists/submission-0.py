# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # heap
        h = []
        for l in lists:
            if l:
                hq.heappush(h, (l.val, id(l), l))

        res = ListNode()
        tail = res
        while h:
            elem = hq.heappop(h)
            tail.next = elem[2]
            tail = tail.next
            if tail.next:
                elemn = tail.next
                hq.heappush(h, (elemn.val, id(elemn), elemn))
        return res.next
            



        