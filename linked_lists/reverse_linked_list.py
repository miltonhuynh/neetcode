"""
206. Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/description/
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Set up two-pointer method
        prev = None
        current = head

        # Keep going until end of list, while current is a node
        while current:
            # Saves current's next node
            temp = current.next
            # Sets current's next node to preverse node (the reversal part)
            current.next = prev
            # Move previous node pointer to current
            prev = current
            # Move current to next node whether or not it exists
            current = temp
        # Returns the new head of the linked list
        return prev