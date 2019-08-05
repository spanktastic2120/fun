    def removeDuplicates(self,head):
        #Write your code here
        node = head
        while node.next:
            if node.data == node.next.data:
                new = node.next.next
                del node.next
                node.next = new
                continue
            node = node.next
        return head
                
      
  
  
  
  
  
  