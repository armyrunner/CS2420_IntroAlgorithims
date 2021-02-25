class Queue:

    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity
        self.capaicty = capacity

    def isFull(self):
        return self.size == self.capapcity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self,item):
        
        if self.isFull():
            return
        
        self.rear = (self.rear + 1) % (self.capacity)
        selfQ[self.rear] = item
        self.size += 1
 
    def DeQueue(self):
        if self.isEmpty():
            return
        self.front = (self.front + 1) % self.capacity
        self.size += 1

