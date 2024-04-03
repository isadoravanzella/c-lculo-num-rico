import math

def f(x):
    return ((x**2+9)/x)*math.asin((6*x)/(x**2+9))-8

e = 0.0001

a = 2
b = 3

k = math.ceil((math.log(b-a,10)-math.log(e,10))/math.log(2,10))

print(k)

for i in range(1,k+1):
    x1=(a+b)/2
    if f(x1)*f(a)<0:
        b = x1
    else:
        a = x1
    print(x1)
