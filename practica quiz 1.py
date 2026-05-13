lista_cuenta= [50.0, -20.3, 100.0, -50.5, -10.0, 200.5]
saldo=0
def saldo_final(lista_cuenta):
    saldo=0
    comision=0
    for plata in lista_cuenta:
        if plata>0:
            saldo+=plata
        else:
            comision= abs(plata)*0.02
            saldo+=plata-comision
    return saldo 
saldo= saldo_final(lista_cuenta)
print(f"El saldo de la cuenta es de {round(saldo,2)}$")