from sympy import *
import math 
def exerciseOne():
    a = []
    a.append(1)
    print(a[0])
    N =1418092
    for n in range(N):
        next = 1 + 2/(1+a[n])
        a.append(next)
        if(n >= 23 and n <= 28):
            #print('n=',n+1,'{:.18f}'.format(math.fabs(a[n]-math.sqrt(3))))
            print(n+1,'=','{:.18f}'.format(a[n]))
    #print('n=',N,'{:.18f}'.format(a[n]-math.sqrt(3)))
    print(N,'=','{:.18f}'.format(a[N]))    




exerciseOne()