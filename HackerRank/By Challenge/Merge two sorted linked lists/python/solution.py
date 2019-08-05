"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if not headA:
        return headB
    if not headB:
        return headA

    if headA.data < headB.data:
        ret = headA
        headA = headA.next
    else:
        ret = headB
        headB = headB.next

    head = ret
    while headA and headB:
        if headA.data < headB.data:
            head.next = headA
            headA = headA.next
        else:
            head.next = headB
            headB = headB.next

        head = head.next

    if headA:
        head.next = headA
    else:
        head.next = headB

    return ret