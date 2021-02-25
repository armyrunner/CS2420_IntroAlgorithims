import random

def RandomDubplicate(List_Length):
    A = []
    for i in range(List_Length):
        r = random.randrange(0,List_Length)
        A.append(r)

    return A

def Mergesort(a):  # counts is an object such[0,0] compare[0],swaps[1]
    lcount = 0
    rcount = 0

    if len(a) == 1:
        return a

    half = len(a)//2

    l = a[0:half]
    r = a[half:]
    # number of swaps counts[1] += 1
    a = Mergesort(r)
    b = Mergesort(l)

    c = []
    
    while rcount < len(a) and lcount < len(b):
        # counts[0]+=1
        if a[rcount] < b[lcount]:
            c.append(a[rcount])
            rcount += 1
        # counts[1] += 1
        else: 
            c.append(b[lcount])
            lcount +=1
            #counts [1] += 1

    if len(a) == rcount:
        c = c + b[lcount:]
    else:
        c = c + a[rcount:]
        #swaps
    return c


def mergesort(a):  # see mersort.py or compare and swap adjustment
    if len(a)<=1:
        return a
    l = a[:len(a)//2]
    r = a[len(a)//2:]
    mergesort(l)
    mergesort(r)
    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(r):
        #c.compares += 1
        if l[i] <= r[j]:
           # c.swaps += 1
            a[k] = l[i]
            k += 1
            i += 1
        else:
           # c.swaps += 1
            a[k] = r[j]
            k += 1
            j += 1
    while i < len(l):
       # c.swaps += 1
        a[k] = l[i]
        k += 1
        i += 1
    while j < len(r):
       # c.swaps += 1
        a[k] = r[j]
        k += 1
        j += 1
    return a


def countsort(a):  # countsort(a,count)
    print(a, "list")
    F = []
    # create list F (Frequency array intalized at 0 for each index)
    for i in range(len(a)):
        F.append(0)
    print(F,"00000")
        # loop through values in and count the number times the value shows up
    for i in range(len(a)):
        F[a[i]] += 1
    print(F, " this the new F")
    # apppend to a the number of times at the index of F
    k = 0 # a list index
    for j in range(len(F)):
       # c.compares += 1
        while F[j] > 0:
           # c.swaps += 1
            a[k] = j  
            F[j] -= 1
            k += 1
    print(a, "new a")
    return a


"""
(lesson)
    merge l and r back over a
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
            k += 1
        else:
            a[k] = r[j]
            j += 1
            k += 1
        while i < len(l):
            a[k]=l[i]
            i += 1
            k += 1
        while j < len(r):
            j += 1
            k += 1
""" 

    

def main():
 
    a = RandomDubplicate(10)
    b = Mergesort(a[:])
    c = mergesort(a[:])
    d = countsort(a[:])
    t = a[:]
    t.sort()


main()