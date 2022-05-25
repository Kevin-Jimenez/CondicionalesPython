#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres 
#con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte 
#al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


name = str(input("Por favor digite su nombre: "))
sex = str(input("Por favor digite 'M' si su sexo es masculino o 'F' si es femenino "))
nueva_cadena = "".join([name[0] for name in name.split()])#Toma la primera letra del nombre

if(nueva_cadena >= 'N' and sex == 'M' ):
    print(f"{name} Perteneces al grupo A")
elif (nueva_cadena <= 'M' and sex == 'F'):
    print(f"{name} Perteneces al grupo A")
else:
    print(f"{name} Perteneces al grupo B")
