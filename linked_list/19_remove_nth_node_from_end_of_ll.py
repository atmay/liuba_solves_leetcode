"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """I used sliding window approach. When rightmost pointer hits end,
    reassign links for the next node for the leftmost pointer"""
    l = r = head
    for _ in range(n):
        r = r.next
    if not r:
        return head.next
    while r.next:
        r = r.next
        l = l.next
    l.next = l.next.next
    return head
