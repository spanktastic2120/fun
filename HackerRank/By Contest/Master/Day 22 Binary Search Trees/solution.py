    def getHeight(self,root):
        #Write your code here
        if not root:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
