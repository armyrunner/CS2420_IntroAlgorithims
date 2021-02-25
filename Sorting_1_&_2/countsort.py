import random

def RandomDubplicate(List_Length):
    A = []
    for i in range(List_Length):
        r = random.randrange(0,List_Length)
        A.append(r)

    return A



def quicksort(A,low,high):

    if len(A) <= 1: # base case
        return A

    # if already presorted it will just return the list
    if (high - low) <= 0: 
        return A

    lmbt = low + 1

    for  i in range(low, high):
        if A[i] < A[low]:
            A[i],A[lmbt] = A[lmbt], A[i]
            lmbt += 1
    A[low], A[lmbt - 1] = A[lmbt - 1], A[low] 

    #low
    quicksort(A,low,lmbt-1)

    #high
    quicksort(A,lmbt,high)

    return A

def main():
 
    a = RandomDubplicate(10)
    print(a)
    c = a[:]
    
    c.sort
    b = quicksort(c,0,len(c))
    #d = quicksort(t,0,len(t),True)
    print(c,"sorted list")

main()
