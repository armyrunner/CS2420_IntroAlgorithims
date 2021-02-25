#PROGRAM 3

import time
import sys
sys.setrecursionlimit(5000)
import math
import random
def createRandomList(num):
    a = []
    for i in range(num):
        a.append(random.randint(0, num))
    return a

class counter():
    def __init__(self):
        self.compares=1
        self.swaps=1

def bubble(a, c):
    done = False
    while done != True:
        done = True
        for i in range(len(a)-1):
            c.compares+=1
            if a[i] > a[i+1]:
                c.swaps+=1
                a[i], a[i+1] = a[i+1], a[i]
                done = False

def shaker(a, c):
    done = False
    upper = len(a)-1
    lower = 0
    while not done and (upper-lower) > 1:
        done=True
        for i in range(lower, upper):
            c.compares+=1
            if a[i] > a[i+1]:
                c.swaps+=1
                a[i], a[i+1] = a[i+1], a[i]
                done = False
        upper -= 1
        
        for i in range(upper, lower, -1):
            c.compares+=1
            if a[i-1] > a[i]:
                c.swaps += 1
                a[i-1], a[i] = a[i], a[i-1]
                done = False
        lower += 1
    return a

def selection(a, c):
    for i in range(len(a)):
        smallestindex = i
        for j in range(i+1, len(a)):
            c.compares+=1
            if a[j] < a[smallestindex]:
                smallestindex = j
        c.swaps+=1
        a[i], a[smallestindex] = a[smallestindex], a[i]
    return a

def merge(a, c):
    if len(a)<=1:
        return a
    l = a[:len(a)//2]
    r = a[len(a)//2:]
    merge(l, c)
    merge(r, c)
    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(r):
        c.compares += 1
        if l[i] > r[j]:
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

def counting(a, c):
    max_value = len(a) + 1
    counting2(a, c, max_value)
    return

def counting2(a, c, max_value):
    m = max_value
    f = [0] * m
    for i in a:
        f[i] += 1
    j = 0
    for i in range(len(f)):
        c.compares += 1
        while f[i] > 0:
            c.swaps+=1
            a[j] = i
            j += 1
            f[i] -= 1
    return a

def quickSort(a, c):
    low = 0
    high = len(a)-1
    quickSort2(a, c, low, high)
    return

def quickSort2(a, c, low, high):
    if high - low <= 0:
        return
    lmgt = low + 1
    for i in range(low+1, high+1):
        c.compares += 1
        if a[i] < a[low]:
            c.swaps += 1
            a[i], a[lmgt] = a[lmgt], a[i]
            lmgt += 1
    pivot = lmgt - 1
    c.swaps += 1
    a[low], a[pivot] = a[pivot], a[low]
    quickSort2(a, c, low, (pivot)-1)
    quickSort2(a, c, pivot+1, high)
    return a

def modQuick(a, c):
    low = 0
    high = len(a)-1
    modQuick2(a, c, low, high)
    return

def modQuick2(a, c, low, high):
    if high - low <= 0:
        return
    mid = (low+high)//2
    mid, low = low, mid
    lmgt = low + 1
    for i in range(low+1, high+1):
        c.compares += 1
        if a[i] < a[low]:
            c.swaps += 1
            a[i], a[lmgt] = a[lmgt], a[i]
            lmgt += 1
    pivot = lmgt - 1
    c.swaps += 1
    a[pivot], a[low] = a[low], a[pivot]
    modQuick2(a, c, low, (pivot)-1)
    modQuick2(a, c, (pivot)+1, high)
    return a
    
def mostlySorted(num):
    b = createRandomList(num)
    b.sort()
    b[0], b[len(b)-1] = b[len(b)-1], b[0]
    return b

def main():
    sorts = [bubble, shaker, selection, merge, counting, quickSort, modQuick]
    print("\t",end="")
    for sort in sorts:
        print(sort.__name__, end='\t')
    print()
    for s in range(3, 13):
        print(s, end='\t')
        for sort in sorts:
            a = createRandomList(2**s)
            b = a[:]
            b.sort()
            c = counter()
            sort(a, c)
            if b != a:
                print("error is sort", sort.__name__)
            print(math.log(c.compares, 2), end='\t')
        print()

main() 
        
