m1= float(input("m1: "))
b1= float(input("b1: "))
m2= float(input("m2: "))
b2= float(input("b2: "))
if(m1==m2):
    if(b1==b2):
        print("Hay puntos infinitos de intersección, las rectas son iguales")
    else:
        print("No hay intersección, las rectas son paralelas")
else:
    x= (b2-b1)/(m1-m2)
    y= m1*x+b1
    print("Intersección en:",(round(x, 2), round(y, 2)))
