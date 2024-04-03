import math

def A(r):
    return (2000/r+250/(math.pi*r**2)+2*math.pi*r**2+math.pi*r+0.125*math.pi)

def f(x):
    return (-2000/(x**2)-500/(math.pi*x**3)+4*math.pi*x+math.pi)

def f1(x):
    return (4000/(x**3)+1500/(math.pi*x**4)+4*math.pi)

e1 = 0.0001
e2 = 0.0001

a = 5
b = 6

x0 = (a+b)/2

x = 1
y = 1
i = 1

while (x>e1)and(y>e2):
    x = abs(f(x0))
    y = abs((x0-f(x0)/f1(x0))-x0)
    x0 = x0-f(x0)/f1(x0)
    print('x',i,' = ',x0)
    i = i+1
    
print('\nA =',A(x0))