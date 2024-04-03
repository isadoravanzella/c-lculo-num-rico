def Elim_Gauss(A,b):
    for j in range(0,len(A)):
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
            
A=[[9,0,-3,0,0],[-4,4,0,0,0],[0,-2,9,0,0],[0,-1,-6,9,-2],[-5,-1,0,0,6]]
b=[120,0,350,0,0]

print('x =',Elim_Gauss(A, b))