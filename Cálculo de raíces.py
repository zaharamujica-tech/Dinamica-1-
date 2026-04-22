a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminante = b**2 - 4*a*c

if discriminante == 0:
    x = -b / (2 * a)
    print("Raíz única:",round(x, 2))

elif discriminante > 0:
    raiz = discriminante**0.5
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    print("Raíces reales:",round(x1, 2),"y",round(x2, 2))

else:
    parte_real = -b / (2 * a)
    parte_imaginaria = (abs(discriminante)**0.5) / (2 * a)
    print("Raíces imaginarias:",round(parte_real, 2),"+",round(parte_imaginaria, 2),"i","y",round(parte_real, 2),"-",round(parte_imaginaria, 2),"i")

