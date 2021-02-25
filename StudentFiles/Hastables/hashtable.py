import math

def Isprime(x):
    if x == 2:
        return True
    
    if x % 2 == 0:
        return False

    s = int(math.sqrt(x))
    for i in range(3,s+1,2):
        if x % i == 0:
            return False
    return True

class Hashtable:

    def __init__(self,expected_size):

        size = expected_size * 2 + 1
        while not Isprime(size):
            size += 2
        self.mTable = [None] * size

    def Exists(self,item):
        key = int(item)
        index = key % len(self.mTable)

        while self.mTable[index] is not None:

            if self.mTable[index] and self.mTable[index] == item:
                return True

            index += 1

            if index >= len(self.mTable):
                index = 0
        return False

    def  Delete(self,item):
        if self.Exists(item):
            key = int(item)
            index = key % len(self.mTable)

            while True:

                if self.mTable[index] and self.mTable[index] == item:
                    self.mTable[index] = False
                    return True

                index += 1
        else:
            return False


    def size(self):

        x = 0
        for item in self.mTable:
            if item:
                x += 1
        return x

    
    def Traverse(self,callback):

        for index in range(len(self.mTable)):
            if self.mTable[index] is not None and self.mTable[index]:
                callback(self.mTable[index])
        
        return

    def Retrieve(self,item):

        key = int(item)
        index = key % len(self.mTable)

        while True:

            if self.mTable[index] is None:
                return None
            if self.mTable[index] and self.mTable[index] == item:
                return self.mTable[index]
            
            index += 1

            if index == len(self.mTable):
                index = 0

    def Insert(self,item):
        if self.Exists(item):
            return False
        
        else:
            index = int(item) % len(self.mTable)
            while self.mTable[index]:
                index += 1

                if index >= len(self.mTable):
                    index = 0
            self.mTable[index] = item
            return True
        

    


        