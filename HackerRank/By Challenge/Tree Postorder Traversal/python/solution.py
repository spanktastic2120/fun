"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    #Write your code here
    import sys
    [postOrder(r) for r in [root.left, root.right] if r]
    sys.stdout.write(str(root.data) + ' ')