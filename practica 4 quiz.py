d=int(input("Ingrese la cantidad de días de medición: "))
descomposicion=[]
completado_antes=False
for i in range(d):
    valor= float(input(f"Ingrese el valor para el día {i+1}: "))
    descomposicion.append(valor)
    if valor>100:
        print("Proceso completado antes de tiempo.")
        completado_antes=True
        break
exceder_50=0
for v in descomposicion:
    if v>50:
        exceder_50+=1
print(f"Lista de descomposición: {descomposicion}")
print(f"Veces se excedió el 50%: {exceder_50}")
if completado_antes==False:
    print("Proceso inconcluso")