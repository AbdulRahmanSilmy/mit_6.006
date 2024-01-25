def direct_access_sort(A):
    u=1+max([a.key for a in A]) #O(n)
    D=[None]*u #O(u)
    for a in A: #O(n)
        D[a.key]=a
    i=0
    for d in D: #O(u)
        if d is not None:
            A[i]=d
            i+=1

def counting_sort(A):
    u=1+max([a.key for a in A]) #0(n)
    D=[[] for _ in range(u)] #O(u)
    for a in A: #O(n)
        D[a.key].append(a)

    i=0
    for chain in D: #O(u)
        for x in chain:
            A[i]=x
            i+=1

def radix_sort(A):
    u = 1 + max([a.key for a in A])
    n = len(A)
    c = 1 + u.bit_length()//n.bit_length()

    D=[]
    class Obj: pass

    for i in range(n): #O(cn)
        D.append(Obj())
        D[i].item=A[i]
        D[i].digits=[]
        high=A[i].key
        for j in range(c):
            high,low=divmod(high,n)
            D[i].digits.append(low)
    
    for i in range(c): #O(cn)
        for j in range(n):
            D[j].key=D[j].digits[i]
        counting_sort(D)
    
    for i,d in enumerate(D): #O(n)
        A[i]=d.item 

    return A

