from stack import Stack
from queue import Queue


class Graphs:


    def __init__(self,numVert):
        self.mNeighbor = []
        for i in range(numVert):
            self.mNeighbor.append([])

    def addEdges(self,V0,V1):
        if V1 is not self.mNeighbor[V0]:
            self.mNeighbor[V0].append(V1)
            return True
        return False

    def isEdges(self,V0,V1):
        edge = self.getNeighbor[V0]
        if V1 in edge:
            return True
        return False

    def getNeighbors(self,v):
        return self.mNeighbor[v]
        
    def findPathDepth(self,V0,V1): 
        s = Stack()
        v = [False] * len(self.mNeighbor)
        s.push(V0)
        v[V0] = True
        while not s.is_empty():
            topstack = s.top()
            if topstack == V1:
                path = []
                while not s.is_empty():
                #for i in range(len(s)):
                    path.append(s.pop())
                path.reverse()
                return path
            # t = s.top()
            nxt = -1
            for n in self.mNeighbor[topstack]:
                if not v[n]:
                    nxt = n
                    break
            if nxt == -1:
                s.pop()
            else:
                s.push(nxt)
                v[nxt] = True
        return None
    
    def findpathBreadth(self,V0,V1):
        # q = Queue()
        q = []
        v = [-1]*len(self.mNeighbor)
        q.append(V0)
        v[V0] = V0
        while len(q) !=  0:
            current = q.pop(0)
            print(current,"this is current")
            if current == V1:
                path = []
                path.append(current)
                i = v[current]
                while not i == V0:
                    path.append(i)
                    i = v[i]
                path.append(V0)
                path.reverse()
                return path
            for n in self.mNeighbor[current]:
                if v[n] == -1:
                    q.append(n)
                    v[n] = current
        return None




