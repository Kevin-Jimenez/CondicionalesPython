#renta anual en euros menos de 10000 5%, entre 10000 y 20000 15%, 
# entre 20000 y 35000 20%, entre 35000 y 60000 30% mas de 60000 45 %

renta = float(input("Ingrese su renta mensual: "))

if (renta <= 10000):
    print("Su renta es del 5%")
elif (renta >= 10000 and renta <= 20000):
    print("Su renta es del 15%")
elif (renta >= 20000 and renta <= 35000):
    print("Su renta es del 20%")
elif (renta >= 35000 and renta <= 60000):
    print("Su renta es del 30%")
else:
    print("Su renta es del 45%")

