"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    #Write your code here
    import sys
    if root.left:
        inOrder(root.left)
    sys.stdout.write(str(root.data) + ' ')
    if root.right:
        inOrder(root.right)