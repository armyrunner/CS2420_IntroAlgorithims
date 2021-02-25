import time
import random
import sys
import math



# creates a random list at any length
def RandomDubplicate(List_Length):
    A = []
    for i in range(List_Length): # use underscore (for _ in range() if i gives trouble
        r = random.randrange(0, List_Length)
        A.append(r)

    return A

class countswapscompares():
    def __init__(self):
        self.compares = 0
        self.swaps = 0

# mostly sorted list
def createsemisort(a):
    b = RandomDubplicate(a)
    b.sort()
    b[0], b[len(b)-1] = b[len(b)-1], b[0]

    return b


def bubblesort(numlist, c):
    flagged = True
    while flagged:
        flagged = False
        for i in range(0, len(numlist)-1):
            c.compares += 1
            if numlist[i] > numlist[i+1]:
                c.swaps += 1
                numlist[i], numlist[i+1] = numlist[i+1], numlist[i]
                flagged = True

    return numlist


def shakersort(numlist, c):
    flagged = True
    while flagged:
        flagged = False
        for i in range(0, len(numlist)-1):
            c.compares += 1
            if numlist[i] > numlist[i+1]:
                c.swaps += 1
                numlist[i], numlist[i+1] = numlist[i+1], numlist[i]
                flagged = True
        for i in range((len(numlist)-2), -1, -1):
            c.compares += 1
            if numlist[i] > numlist[i+1]:
                c.swaps += 1
                numlist[i], numlist[i+1] = numlist[i+1], numlist[i]
                flagged = True
    return numlist


def selectionsort(numlist,c):
    for i in range(len(numlist)):
        smIndex = i
        for j in range(i+1, len(numlist)):
            c.compares += 1
            if numlist[j] < numlist[smIndex]:
                smIndex = j
        c.swaps += 1
        numlist[i], numlist[smIndex] = numlist[smIndex], numlist[i]
    return numlist


def mergesort(a,c):  # see mersort.py or compare and swap adjustment
    if len(a)<=1:
        return a
    l = a[:len(a)//2]
    r = a[len(a)//2:]
    mergesort(l, c)
    mergesort(r, c)
    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(r):
        c.compares += 1
        if l[i] <= r[j]:
            c.swaps += 1
            a[k] = l[i]
            k += 1
            i += 1
        else:
            c.swaps += 1
            a[k] = r[j]
            k += 1
            j += 1
    while i < len(l):
        c.swaps += 1
        a[k] = l[i]
        k += 1
        i += 1
    while j < len(r):
        c.swaps += 1
        a[k] = r[j]
        k += 1
        j += 1
    return a


def countsort(a,c):  # countsort(a,count)
    F = []
    # create list F (Frequency array intalized at 0 for each index)
    for i in range(len(a)):
        F.append(0)
        # loop through values in and count the number times the value shows up
    for i in range(len(a)):
        F[a[i]] += 1
    # apppend to a the number of times at the index of F
    k = 0 # a list index
    for j in range(len(F)):
        c.compares += 1
        while F[j] > 0:
            c.swaps += 1
            a[k] = j  
            F[j] -= 1
            k += 1
    return a


def quicksort(a, low, high, mod,c):

    # if len(a) <= 1:  # base case
    #     c.compare += 1
    #     return a

    # if already presorted it will just return the list
    if (high - low) <= 0:
        c.compares += 1
        return a

    if mod:
        mid = (low + high) // 2
        a[low], a[mid] = a[mid], a[low]
        
    lmbt = low + 1

    for i in range(low, high):
        c.compares += 1
        if a[i] < a[low]:
            c.swaps += 1
            a[i], a[lmbt] = a[lmbt], a[i]
            lmbt += 1
    c.swaps += 1
    a[low], a[lmbt - 1] = a[lmbt - 1], a[low]

    # low
    quicksort(a, low, lmbt-1, mod,c)

    # high
    quicksort(a, lmbt, high, mod,c)
    c.swaps += len(a[low : lmbt])
    c.swaps += len(a[lmbt + 1: high])

    return a

def bquicksort(a,counts):
	quick =  quicksort(a, 0, len(a), False,counts)
	return quick

def mquicksort(a,counts):
	modquick = quicksort(a, 0, len(a), True,counts)
	return modquick

def main():

    sys.setrecursionlimit(5000)
    print(" ",end="\t")
    sorts = [bubblesort,shakersort,selectionsort,mergesort,bquicksort,mquicksort,countsort]
    sortnames = ["bubblesort","shakersort","selectionsort","mergesort","quicksort","modquick","countsort"]


    for i in range(len(sortnames)):
        print(sortnames[i],end='\t')
    print()

    for i in range(3,13):
        print(i, end='\t')
        for sort in sorts:
            a =createsemisort(2**i)
            b = a[:]
            b.sort()
            c = countswapscompares()
            sort(a,c)
            if b != a:
                print("error",sort.__name__)
            print('%8.2f' % (math.log(c.compares,2)), end="\t")
        print()

if __name__ == "__main__":
    main()

