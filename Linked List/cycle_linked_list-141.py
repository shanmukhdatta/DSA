## problem statemnt foer the leetcode 141
## Leetcode 141. Linked List Cycle
## Given the head of a linked list, determine if the linked list has a cycle in it.

class solution:
    def hasCycle(self, head):
        ## using the slow and fast pointer approach
        slow = head
        fast = head
        while fast and fast.next:
            ## fast pointer moves two steps at a time
            fast = fast.next.next
            ## slow pointer moves one step at a time
            slow = slow.next
            ## if the slow and fast pointer meet, then there is a cycle
            if slow == fast:
                return True
        return False
        