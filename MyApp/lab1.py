import math

a = int(input("Введите первый коэффициент "))
b = int(input("Введите второй коэффициент "))
c = int(input("Введите третий коэффициент "))
D = b*b - 4*a*c
sqrtD = math.sqrt(D)
if D < 0:
    print("Решений нет.")
elif D==0:
    x = -b / 2 / a
    print(x)
else:
    x1 = (-b + sqrtD)/(2*a)
    x2 =(-b - sqrtD)/(2*a)
    print("x1=", x1, "x2=", x2)