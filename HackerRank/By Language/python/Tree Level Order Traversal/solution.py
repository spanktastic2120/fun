"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    #Write code Here
    from collections import deque
    import sys
    Q = deque()
    Q.append(root)
    while Q:
        root = Q.popleft()
        sys.stdout.write(str(root.data) + ' ')
        [Q.append(r) for r in [root.left, root.right] if r]