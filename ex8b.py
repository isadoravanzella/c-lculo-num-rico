def Elim_Gauss(A,b):
    for j in range(0,len(A)):
        c= j
        for a in range(j+1,len(A)):
            if A[a][j]>A[j][j]:
                c = a
        v=A[j]
        v1=b[j]
        
        A[j]=A[c]
        A[c]=v
        
        b[j]=b[c]
        b[c]=v1
        
        for k in range(j+1,len(A)):
            m= A[k][j]/A[j][j]
            for i in range(j,len(A)):
                A[k][i]=A[k][i]-m*A[j][i]
            b[k]=b[k]-m*b[j]
    
    v=[]
    for k in range(len(b)-1,-1,-1):
        soma=0
        for j in range(k+1,len(b)):
            soma=soma+A[k][j]*v[len(b)-1-j]
        v.append((b[k]-soma)/A[k][k])
    
    x=[]
    for k in range(0,len(v)):
        x.append(v[len(v)-1-k])
        
    return x
            
A=[[0.0002,3,-1],[4,0.0005,3],[-1,-1,10]]
b=[4,6,1]

print('x =',Elim_Gauss(A,b))