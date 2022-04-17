"""
You are given the head of a linked list, which contains a series of integers separated by 0's.
The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value
is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation:
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_nodes(self, head: ListNode | None) -> ListNode | None:
        """
        I used 2 pointers approach. As it says, head.val always equals to zero, so I assigned pointer 1 to the head and
        started adding up values of next nodes by moving second pointer step by step until value of node wasn't 0.
        In this case I moved the first pointer to the next node, assigned combined value to it and restarted
        calculating sum of nodes. When pointer 2 reached the end of the linked list, I marked next node of pointer 1 as
        None and returned head.next.

        """
        p1 = head
        p2 = head.next
        val = 0
        while p2:
            if p2.val == 0:
                p1 = p1.next
                p1.val = val
                val = 0
            else:
                val += p2.val
            p2 = p2.next
        p1.next = None
        return head.next
