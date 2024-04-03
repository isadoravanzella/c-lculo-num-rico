import numpy as np

def Fatoracao(A):
    L=[]
    
    for i in range(0,len(A)):
        v=[]
        for j in range(0,len(A)):
            if i==j:
                v.append(1)
            else:
                v.append(0)
        L.append(v)
    
    for j in range(0,len(A)):
        for k in range(j+1,len(A)):
            m= A[k][j]/A[j][j]
            L[k][j]=m
            for i in range(j,len(A)):
                A[k][i]=A[k][i]-m*A[j][i]
                
    U = A
    
    return U,L

A=[[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]

L1 = np.array(Fatoracao(A)[1])
U1 = np.array(Fatoracao(A)[0])

print('L = ')
print(L1)
print('U = ')
print(U1)