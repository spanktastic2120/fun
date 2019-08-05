"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    #Write your code here
    import sys
    from collections import deque
    Q = deque()
    top = root
    while root.left:
        Q.appendleft(root.left)
        root = root.left

    Q.append(top)
    root = top

    while root.right:
        Q.append(root.right)
        root = root.right

    print ' '.join([str(q.data) for q in Q])