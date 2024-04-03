def Fatoracao(A, b):
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
                
    y=[]
    for k in range(0,len(b)):
        soma=0
        for j in range(0,k):
            soma = soma + L[k][j]*b[j]
        y.append(b[k]-soma)
        
    v=[]
    for k in range(len(y)-1,-1,-1):
        soma=0
        for j in range(k+1,len(y)):
            soma=soma+U[k][j]*v[len(v)-j]
        v.append((y[k]-soma)/U[k][k])
    
    x=[]
    for k in range(0,len(v)):
        x.append(v[len(v)-1-k])
        
    return x
            
A=[[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]
b=[-1.2,7.8,3.5]

print('x = ',Fatoracao(A,b)) 


