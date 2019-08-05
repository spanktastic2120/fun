"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if not head:
        return Node(data)
    if data < head.data:
        n = Node(data, head, None)
        head.prev = n
        return n
    
    else:
        ret = head

    while head:
        if data < head.data:
            n = Node(data, head, head.prev)
            if head.prev:
                head.prev.next = n
            head.prev = n
            break
        elif head.next == None:
            head.next = Node(data, None, head)
            break
        head = head.next

    return ret