    def levelOrder(self,root):
  	    #Write your code here
        q = [root]
        string = ''
        while q:
            string += str(q[0].data) + ' '
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            q.pop(0)
        print string
                