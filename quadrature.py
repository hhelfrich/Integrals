import numpy as np 

def QuadLeft(f, a, b, dx):
    N = int((b-a)/dx)+1
    dx = float((b-a)/N)
    result = 0
    for i in range(0, N):
        x = (i*dx)+a
        result += f(x)*dx
    return result

def QuadRight(f, a, b, dx):
    N = int((b-a)/dx)+1
    dx = float((b-a)/N)
    result = 0
    for i in range(0, N):
        x = (i+1)*dx+a
        result += f(x)*dx
    return result

def QuadCenter(f, a, b, dx):
    N = int((b-a)/dx)+1
    dx = float((b-a)/N)
    result = 0
    for i in range(0, N):
        x = (i+0.5)*dx+a
        result += f(x)*dx
    return result

def QuadTrap(f, a, b, dx):
    N = int((b-a)/dx)+1
    w = np.full(N, 1.0)
    w[0] = w[N-1] = 0.5
    x = np.linspace(a, b, len(w))
    dx = x[1]-x[0]
    y = w*f(x)
    return np.sum(y)*dx