"""En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden 
ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la 
puntuación del nivel."""

evaluacion = float(input("Por favor ingrese la evaluacion del empleado, recuerde que los valores deben ser '0.0, 0.4, 0.6': "))
total = 2400 * evaluacion

if(evaluacion == 0.0):
    print(f"La puntuacion fue {evaluacion} INACEPTABLE\nPago: {total}€")
elif (evaluacion == 0.4):
    print(f"La puntuacion fue {evaluacion} ACEPTABLE\nPago: {total}€")
elif(evaluacion >= 0.6):
    print(f"La puntuacion fue {evaluacion} MERITORIO\nPago: {total}€")