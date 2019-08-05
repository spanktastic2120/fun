    def insert(self,head,data): 
    #Complete this method
        if not head:
            self.tail = self.head = Node(data)
        else:
            self.tail.next = self.tail = Node(data)
        return self.head