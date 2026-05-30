# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        result_head = result_curr = ListNode()
        
        # use a min heap
        for i, head in enumerate(lists):
            if not head:
                continue
            
            heapq.heappush(min_heap, (head.val, i, head))

        while min_heap:    
            # heappop from min_heap, add to result, then heappush its next node back into heap
            val, i, curr = heapq.heappop(min_heap)
            if curr.next:
                heapq.heappush(min_heap, (curr.next.val, i, curr.next))
            
            result_curr.next = curr
            result_curr = result_curr.next

        return result_head.next
