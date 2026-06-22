## comment for problem statemnt 
## Leetcode 19. Remove Nth Node From End of List
## Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ## using left and right pointer approach
        dummy = ListNode(0,head)
        left = dummy
        right = head

        ## move right to start postion
        while n>0 and right:
            right = right.next
            n-=1
        
        ## to move left andd rihght ot correct postions

        while right:
            left = left.next
            right = right.next

        ## delete the node

        left.next = left.next.next

        return dummy.next

        
