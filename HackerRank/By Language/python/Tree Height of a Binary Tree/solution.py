# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root, h=None):
    h = h if h else 0
    if not any([root.right, root.left]):
        return h
    
    elif all([root.right, root.left]):
        return max([height(root.left, h+1), height(root.right, h+1)])

    else:
        return height(root.left, h+1) if root.left else height(root.right, h+1)

