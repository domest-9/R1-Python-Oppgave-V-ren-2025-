from pylab import *
from scipy.optimize import curve_fit

år = [0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,21]
poeng = [88,100,72,107,170,30,170,51,47,33,185,372,62,218,365,261,344,274,334,250,310]

def f(x,a,b,c):
    return c/(1+a*exp(-b*x))

a_s = 1000
b_s = 0.1
c_s = 1000

[a,b,c] = curve_fit(f,år,poeng, p0 = [a_s,b_s,c_s])[0]
print("a =", round(a,1))
print("b =", round(b,2))
print("c =", round(c,1))

plot(år,poeng,"o")
x = linspace (0, 100, 1000)
plot(x, f(x, a, b, c), "r")
show()