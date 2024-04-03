import math

def f(x):
    return (math.sin(x)+x-2)

def f1(x):
    return (math.cos(x)+1)

e1 = 0.0001
e2 = 0.0001

a = math.pi/4
b = math.pi/2

x0 = (a+b)/2

x = 1
y = 1

while (x>e1)and(y>e2):
    x = abs(f(x0))
    y = abs((x0-f(x0)/f1(x0))-x0)
    x0 = x0-f(x0)/f1(x0)
    print(x0)
    
    