"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    #Enter you code here.
    if not r:
        return Node(val)

    if val < r.data:
        if r.left:
            insert(r.left, val)
        else:
            r.left = Node(val)
    elif val > r.data:
        if r.right:
            insert(r.right, val)
        else:
            r.right = Node(val)
    return r