class Solution:
    # Write your code here
    def __init__(self):
        self.queue = []
        self.stack = []
    
    def pushCharacter(self, c):
        self.stack.append(c)
        
    def enqueueCharacter(self, c):
        self.queue.append(c)
        
    def popCharacter(self):
        return self.stack.pop(-1)
        
    def dequeueCharacter(self):
        return self.queue.pop(0)