from graphs import Graphs
from stack import Stack

def main():
    

    fin = open("input.txt","r")

    numVert = int(fin.readline())
    numEdges = int(fin.readline())
    
    g = Graphs(numVert)

    for i in range(numEdges):
        pair = fin.readline()
        numbers = pair.split()
        V0 = int(numbers[0])
        V1 = int(numbers[1])
        g.addEdges(V0,V1)

    testcases = int(fin.readline())

    for i in range(testcases):
        pair = fin.readline()
        testnumbers = pair.split()
        V0 = int(testnumbers[0])
        V1 = int(testnumbers[1])
        depthsearch = g.findPathDepth(V0,V1)
        # print("Depth Search is", depthsearch)
        #breadthsearch = g.findpathBreadth(V0,V1)
        print("Breadth Search is",depthsearch)

main()
