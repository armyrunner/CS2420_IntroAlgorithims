
class Stack:

    def __init__(self):
        self.mItems = []
        
    def getItem(self):
        return self.mItems
    
    def top(self):
        return self.mItems[len(self.mItems)-1]

    def push(self,char):
        return  self.mItems.append(char)

    def is_empty(self):
        return len(self.mItems) == 0
       
    def pop(self):
        if len(self.mItems) > 0:
            value = self.mItems[len(self.mItems)-1]
            self.mItems.pop()
        else:
            raise Exception("Trying to pop form an empty stack.")
        return value
