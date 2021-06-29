
print(""" elija una moneda base:
1 - Dolar
2 - Peso
3 - Euro """)
print("---------------------------")
moneda1 = int(input("moneda base:"))
print("""elija a que moneda desea convertir:
1 - Dolar
2 - Peso
3 - Euro""" )
print("---------------------------")
moneda2 = int(input("moneda a convertir:"))
print("---------------------------")

#dolares a pesos
if moneda1 == 1 and moneda2 == 2:
    print("U$S/AR$")
    monto = int(input("ingrese el monto en Dolares:"))
    conver1 = monto * 95.51
    print("ARS",conver1)
    
#dolares a euro
if moneda1 == 1 and moneda2 ==3:
     print("U$S/EUR")
     monto = int(input("ingrese el monto en Dolares:"))
     conver1 = monto * 0.84
     print("EUR",conver1)       
    
# peso a dolar    
if moneda1 == 2 and moneda2 == 1:
     print("AR$/U$S")
     monto = int(input("ingrese el monto en pesos:"))
     conver1 = monto * 0.010
     print("U$S",conver1)
     
# pesos a euros     
if moneda1 == 2 and moneda2 == 3:
     print("AR$/EUR")
     monto = int(input("ingrese el monto en pesos:"))
     conver1 = monto * 0.0088
     print("EUR",conver1)
     
#Euro a pesos     
if moneda1 == 3 and moneda2 ==2:
     print("EUR/AR$")
     monto = int(input("ingrese el monto en Euros:"))
     conver1 = monto * 113.80
     print("AR$",conver1)
     
#Euro a dolar
if moneda1 == 3 and moneda2 ==1:
     print("EUR/U$S")
     monto = int(input("ingrese el monto en Euros:"))
     conver1 = monto * 1.19
     print("U$S",conver1)