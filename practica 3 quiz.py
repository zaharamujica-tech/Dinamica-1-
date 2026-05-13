n=int(input("Ingrese la cantidad de lotes a evaluar: "))
lote_n=1
lotes=[]
lista_temperatura=[]
lista_concentracion=[]
while len(lotes)<n:
    temperatura=int(input(f"Ingrese la temperatura del {lote_n} lote: "))
    concentracion=int(input(f"Ingrese la concentracion del {lote_n} lote: "))
    lotes.append((temperatura,concentracion))
    lista_temperatura.append(temperatura)
    lista_concentracion.append(concentracion)
    lote_n+=1
def evaluar_lotes (lista_temperatura, lista_concentracion):
    temperatura_mayor_100=0
    promedio_concentracion=0
    promedio_temperatura=0
    inestabilidad="no"
    promedio_temperatura=sum(lista_temperatura)/len(lista_temperatura)
    for lote_t in lista_temperatura:        
        if lote_t>100:
            temperatura_mayor_100+=1
    for lote_c in lista_concentracion:
        promedio_concentracion= sum(lista_concentracion)/len(lista_concentracion)
    if promedio_temperatura>promedio_concentracion:
        inestabilidad="si"
    return promedio_concentracion, temperatura_mayor_100, promedio_concentracion, inestabilidad 
promedio_temperatura, temperatura_mayor_100, promedio_concentracion, inestabilidad=evaluar_lotes (lista_temperatura, lista_concentracion)
print(f"Información de la lista de lotes {lotes}:")
print(f"Lotes con temperatura mayor a 100: {temperatura_mayor_100}")
print(f"Promedio de concentración: {round(promedio_concentracion)}")
print(f"El proceso {inestabilidad} es inestable")