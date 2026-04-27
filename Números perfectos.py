numero=int(input("Ingrese un número: "))
divisor=1
suma_divisores=0
while (divisor<numero):
    if(numero%divisor==0):
        suma_divisores+=divisor
    divisor+=1
if(suma_divisores==numero):
    print(f"{numero} es un número perfecto")
else:
    print(f"{numero} no es un número perfecto")