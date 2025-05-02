from pylab import *
from scipy.optimize import curve_fit

def f(x):
    return 86.1*1.065**(x-2000)

def g(x):
    return 84.79*1.03**(x-2000)

def main():
    x = linspace(2000, 2030, 1000)
    y1 = f(x)
    y2 = g(x)

    plot(x, y1, label='$f(x) = 86.1 \cdot 1.065^x$ Sverige', color='gold', linewidth=3)
    plot(x, y2, label='$g(x) = 84.79 \cdot 1.03^x$ Norge', color='red', linewidth=3)

    xlabel('Årstall')
    ylabel('Poeng')
    legend()
    grid()
    show()

    x_input = float(input("Skriv inn et årstall (f.eks. 2030): "))

    y1_value = f(x_input)
    y2_value = g(x_input)

    print(f"I år {int(x_input)} får Sverige {round(y1_value, 0)} poeng")
    print(f"I år {int(x_input)} får Norge {round(y2_value, 0)} poeng")

if __name__ == "__main__":
    main()