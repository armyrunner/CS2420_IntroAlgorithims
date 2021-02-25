import random
#import sys


def RandomDubplicate(List_Length):
    A = []
    for i in range(List_Length):
        r = random.randrange(0,List_Length)
        A.append(r)

    return A

def bubblesort(numlist):
    flagged= True
    while flagged:
        flagged = False
        for i in range(0,len(numlist)-1):
            if numlist[i] > numlist[i+1]:
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp
                flagged = True

    return numlist


def shakersort(numlist):
    flagged= True
    while flagged:
        flagged = False
        for i in range(0,len(numlist)-1):
            if numlist[i] > numlist[i+1]:
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp
                flagged = True
        for i in range((len(numlist)-2),-1,-1):
            if numlist[i] > numlist[i+1]:
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp
                flagged = True
    return numlist

def selectionsort(numlist):
    
    for i in range(len(numlist)-1):
        smallnum = 0
        for j in range(i+1,len(numlist)):
            smIndex = j
            if numlist[i] > numlist[smIndex]:
                smallnum = numlist[i]
                smIndex = j
                numlist[i],numlist[smIndex] = numlist[smIndex],numlist[i]
    return numlist


def mergesort(a):  # see mersort.py or compare and swap adjustment
    lcount = 0
    rcount = 0

    if len(a) == 1:
        return a

    half = len(a)//2

    l = a[0:half]
    r = a[half:]

    a = mergesort(r)
    b = mergesort(l)

    c = []
    
    while rcount < len(a) and lcount < len(b):
        
        if a[rcount] < b[lcount]:
            c.append(a[rcount])
            rcount += 1
        else:
            c.append(b[lcount])
            lcount +=1

    if len(a) == rcount:
        c = c + b[lcount:]
    else:
        c = c + a[rcount:]
    return c

def countsort(a):# countsort(a,count)
    F = []
    #create list F (Frequency array intalized at 0 for each index)
    for i in range(len(a)): 
        F.append(0)
        #loop through values in and count the number times the value shows up
    for i in range(len(a)):
        F[a[i]] += 1
    # apppend to a the number of times at the index of F
    a = []
    for j in range(len(F)):
        for k in range(F[j]):
            a.append(j)
            #counts[1] += len(a)
            #counts[0] += len(a)
 
    return a

def quicksort(a,low,high,mod):
    
    if len(a) <= 1: # base case
        return a

    # if already presorted it will just return the list
    if (high - low) <= 0:
        return a

    if mod:
        mid = (low + high )// 2
        a[low], a[mid] = a[mid], a[low] 


    lmbt = low + 1

    for  i in range(low, high):
        if a[i] < a[low]:
            a[i],a[lmbt] = a[lmbt], a[i]
            lmbt += 1
    a[low], a[lmbt - 1] = a[lmbt - 1], a[low] 

    #low
    quicksort(a,low,lmbt-1,mod)

    #high
    quicksort(a,lmbt,high,mod)

    return a


def main():

        #sys.setrecursionlimit(5000)

        print( "  ")
        numlist = RandomDubplicate(10)
        b = numlist[:]
        b.sort()
        

        print(numlist , "Orginal List")
        print(b , "Sorted By Python")

        bsort = bubblesort(numlist[:])
        print(bsort , "Bubble Sort ")

        Shaker = shakersort(numlist[:])
        print(Shaker , "Shaker Sort ")

        Selector = selectionsort(numlist[:])
        print(Selector, "Selector Sort ")

        merge = mergesort(numlist[:])
        print(merge, "Merge Sort ")

        quick = quicksort(numlist[:],0,len(numlist),False)
        print(quick, "Quick Sort ")

        modquick = quicksort(b[:],0,len(b),True)
        print(modquick, "Modified Quick Sort ")

        count = countsort(numlist[:])
        print(count, "Count Sort")

        print( "  ")



if __name__ == "__main__":
    main()



"""

new fucntion basic quick sort(a,counts)
    call the function

new funciton quicksortmodified(a,counts)
    call the function

def createmostly sorted list(a)
    a = create list my list
    a.sort()
    a[i],a[-1] = a[-1],a[i]
    return a

"""


"""

2 for loops
1 for loop for all the functions that do the sorting loop
1 for the problem size

sorts = [list of all seven sorts]

print("",end="\t")
for sort in sorts:
    print(sort.__name__,end="\t")
    print()

for lsize in range(3,13):
    size = 2**lsize
    print(lsize, end="\t")
    for sort in sorts:
        a = randomduplicatelist(size)
        b = [:]
        counts = [0,0]
        sort(a,counts)
        If a != b:
            print("error")
        print(math.log(counts[0] + 1,2), end="\t")
    print()




"""