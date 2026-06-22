## problem statemnt of th e leetcode 21
## Leetcode 21. Merge Two Sorted Lists
## You are given the heads of two sorted linked lists list1 and list2.
## Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
## Return the head of the merged linked list.

from typing import ListNode, Optional
class solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        ## using the dummy node aprroach

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1 ## appending the list1 node to the dummy node
                l1 = l1.next
            else:
                tail.next = l2 ## appending the list2 node to the dummy node
                l2 = l2.next
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2
        return dummy.next



