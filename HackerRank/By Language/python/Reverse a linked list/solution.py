"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    rev = []
    while head:
        rev.append(head)
        head = head.next
    ret = rev[-1]
    head = ret
    for i in rev[-2::-1]:
        head.next = i
        head = head.next
    head.next = None
    return ret
        