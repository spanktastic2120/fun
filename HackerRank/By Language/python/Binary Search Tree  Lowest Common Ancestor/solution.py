"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
    #Enter your code here
    if not((v1 < root.data and v2 < root.data) or (v1 > root.data and v2 > root.data)):
        return root

    while root:
        if v1 < root.data:
            root = root.left
        else:
            root = root.right
        if not((v1 < root.data and v2 < root.data) or (v1 > root.data and v2 > root.data)):
            return root