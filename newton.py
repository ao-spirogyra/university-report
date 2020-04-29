import matplotlib.pyplot as plt
import numpy as np
def func(x):
    return x ** 2 + 2*x + 1

def differentialFunc(x):
    return 2*x + 2

def newton(initial_x):
    x = np.linspace(-10,10,200)
    max_loop = 199
    x_n = [initial_x]
    # x_n.append()
    next_x = 0
    for i in range(max_loop):
        next_x = x_n[i] - func(x_n[i])/differentialFunc(x_n[i])
        x_n.append(next_x)
        plt.plot(x_n[i],func(x_n[i]),marker = 'o')
    return x_n

if __name__ == '__main__':
    approximating_x = newton(2)
    x = np.linspace(-5,3,200)
    y = x ** 2 + 2*x + 1
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y', rotation = 0)
    plt.title('newton approximation')
    plt.show()