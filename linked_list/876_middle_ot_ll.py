"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node_bruteforce(self, head: Optional[ListNode]) -> Optional[ListNode]:
    lst = []
    cur = head
    while cur.next:
        lst.append(cur)
        cur = cur.next
    lst.append(cur)

    return lst[len(lst) // 2]


def middle_node(head: ListNode) -> ListNode:
    """Tortoise and hair approach"""
    p_slow = head
    p_fast = head
    while p_fast and p_fast.next:
        p_slow = p_slow.next
        p_fast = p_fast.next.next
    return p_slow
