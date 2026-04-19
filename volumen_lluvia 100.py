volumen_lluvia = 100
volumen_reservorio = 100
volumen_lluvia= volumen_lluvia-10
volumen_reservorio = volumen_reservorio + volumen_lluvia
volumen_reservorio= volumen_reservorio+ volumen_reservorio*5/100
volumen_reservorio= volumen_reservorio- volumen_reservorio*2/100
volumen_reservorio= volumen_reservorio- 2.5*10**5
print (volumen_reservorio)





