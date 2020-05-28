import matplotlib.pyplot as plt
import numpy as np
import math
def func(x):
    return x**5-4

def differentialFunc(x):
    return 5*(x**4)

def newton(initial_x):
    
    max_loop = 49
    x_n = [initial_x]
    # x_n.append()
    next_x = 0
    for i in range(max_loop):
        next_x = x_n[i] - func(x_n[i])/differentialFunc(x_n[i])
        x_n.append(next_x)
        plt.plot(x_n[i],func(x_n[i]),marker = 'o', color = 'g')
        if(i+1 <= 6):
          print(x_n[i]-1.319507910772894)
        if(func(x_n[i+1])< 10**(-12)):
          print(i+1,'で収束f(x)=','{:.12}'.format(func(x_n[i+1])))
    return x_n

if __name__ == '__main__':
    approximating_x = newton(1)
    x = np.linspace(-5,3,200)
    y = math.e**x-5*x
    plt.plot(x, y, color = 'b')
    plt.xlabel('x')
    plt.ylabel('y', rotation = 0)
    plt.title('newton approximation')
    plt.show()