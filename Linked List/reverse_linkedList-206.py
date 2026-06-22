## comment gives the problem statemnet of the leetcode 206
## Leetcode 206. Reverse Linked List
## Given the head of a singly linked list, reverse the list, and return the reversed list.

#--------------  recursive approach ---------------------------

from typing import Optional
def reverse_recursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_recursive(head.next)
    
    head.next.next = head
    head.next = None
    
    return new_head



#-------------- iterative approach ---------------------------
class solution:
    def reverseList(self, head ):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

