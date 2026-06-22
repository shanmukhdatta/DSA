## problem statemnt for leetcode 143
## Leetcode 143. Reorder List
## You are given the head of a singly linked list. The nodes in the list are sequentially numbered 1, 2, 3, ..., n.
## Reorder the list so that the nodes are in the following order: 1 → n → 2 → n-1 → 3 → n-2 → ... → (n/2) → (n/2)+1
## Return the head of the reordered list.

class solution:
    def reorderList(self, head):
        slow,fast = head, head.next
        ## finding the middle of the list at slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        ## reverse the list at second.next
        second = slow.next 
        slow.next = None ## break connect between the first and second
        prev = None
        

        # reverse the second list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        ## merging two lists
        second = prev
        first = head

        while second:
            temp1, temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        

        