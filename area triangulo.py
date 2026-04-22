a= float(input("Ingrese la longitud de a: "))
b= float(input("Ingrese la longitud de b: "))
c= float(input("Ingrese la longitud de c: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"El área del triángulo es: {round(area,2)}")