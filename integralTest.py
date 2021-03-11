from quadrature import Quadleft, QuadRight, QuadCenter, QuadTrap

def f(x):
    return (x-2)**3 - 3.5*x + 8

dx = 1E-3

print("QuadLeft Result is: ", QuadLeft(f, 0, 4, dx))

print("QuadRight Result is: ", QuadRight(f, 0, 4, dx))

print("QuadCenter Result is: ", QuadCenter(f, 0, 4, dx))

print("QuadTrap Result is: ", QuadTrap(f, 0, 4, dx))
