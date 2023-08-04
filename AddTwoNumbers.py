# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_last_iteration(ln1: ListNode, ln2: ListNode) -> bool:
    return (ln1 is None or ln1.next is None) and (ln2 is None or ln2.next is None)


def print_tree_as_list(li: Optional[ListNode]):
    res = []
    node = li

    while node is not None:
        res.append(node.val)
        node = node.next

    print(res)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pn = None  # parent node

        cn1 = l1
        cn2 = l2
        mind = 0
        crn = None  # current node

        while True:

            summ = ((cn1.val if cn1 is not None else 0) +
                    (cn2.val if cn2 is not None else 0) +
                    mind)

            if summ >= 10:
                summ = summ - 10
                mind = 1
            else:
                mind = 0

            # print(cn1.val if cn1 is not None else 0, cn2.val if cn2 is not None else 0, summ, mind,
            #       print_tree_as_list(pn))

            node = ListNode(summ)

            if crn is None:
                crn = node
                pn = node
            else:
                crn.next = node
                crn = crn.next

            if is_last_iteration(cn1, cn2):
                if mind != 0:
                    crn.next = ListNode(mind)
                break

            if cn1 is not None:
                cn1 = cn1.next

            if cn2 is not None:
                cn2 = cn2.next

        return pn


# tl1 = tree_to_list(
#     ListNode(2, ListNode(4, ListNode(3)))
# )
# tl2 = tree_to_list(
#     ListNode(5, ListNode(6, ListNode(4)))
# )

# tl1 = tree_to_list(
#     ListNode(0)
# )
# tl2 = tree_to_list(
#     ListNode(0)
# )

tl1 = ListNode(9,
               ListNode(9,
                        ListNode(9,
                                 ListNode(9,
                                          ListNode(9,
                                                   ListNode(9,
                                                            ListNode(9)
                                                            )
                                                   )
                                          )
                                 )
                        )
               )

tl2 = ListNode(9,
               ListNode(9,
                        ListNode(9,
                                 ListNode(9)
                                 )
                        )
               )

solution = Solution()
print_tree_as_list(solution.addTwoNumbers(tl1, tl2))
