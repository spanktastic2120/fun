"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    #Write your code here
    import sys
    sys.stdout.write(str(root.data) + ' ')
    [preOrder(r) for r in [root.left, root.right] if r]