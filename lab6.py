from os import system
from math import sqrt

def cub_rt(x):  # підпрограма, що обчислює кубічний корінь числа
    limit = int(x)
    z = x
    n = 0
    while(n < x):
        z = (1 / 3) * (x / (z ** 2) + 2 * z) # формула для обчислення кореня з умови
        n = n + 1
    return z

def equation(a, b):  # підпрограма, що підставляє значення а i b до заданої формули для Y
    return round(cub_rt(cub_rt(a)) + sqrt(cub_rt(b)) + cub_rt(a + b), 5)

def main():
    a = float(input("a = "))
    b = float(input("b = "))
    if a > 0 and b > 0:  # обмеження на значення, задані в умові
        Y = equation(a, b)
        print("Y = ", Y, "\n")
    else:
        print("Invalid input!")
    system("pause")

if __name__ == '__main__':
    main()