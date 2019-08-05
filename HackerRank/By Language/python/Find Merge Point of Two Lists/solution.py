"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    A = set()
    while headA:
        A.add(headA.data)
        headA = headA.next
    while headB:
        if headB.data in A:
            return headB.data
        headB = headB.next