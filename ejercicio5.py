# Para tributar un determinado impuesto se debe ser mayor de 16 años 
#y tener unos ingresos iguales o superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y 
#muestre por pantalla si el usuario tiene que tributar o no.

age = int(input("Please digit yout age: "))
salary = float(input("Please digit your salary in euros: "))

if(age >= 16 and salary >= 1000):
    print("Should tributar")
else:
    print("Shouldn't tributar")
