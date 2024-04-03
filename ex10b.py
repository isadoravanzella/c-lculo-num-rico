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

def Det(A):
    U1 = Fatoracao(A)[0]
    produto = 1
    for k in range(0,len(A)):
        produto=produto*U1[k][k]
    
    return produto

A=[[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]

print(Det(A))