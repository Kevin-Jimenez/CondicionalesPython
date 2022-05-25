"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.
    Ingredientes vegetarianos: Pimiento y tofu.
    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de 
su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir 
un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe 
mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""


print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
pizza = input("Por favor digite el numero de menu que te gustaria: ")

if (pizza == "1"):
    print("Ingredientes de pizzas vegetarianas\n\t 1) Pimiento\n\t 2) Tofu\n")
    complemento = input("¿Que ingrediente deseas?: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")#el end pone el valor que ingresamos en el print
    if (complemento == "1"):
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1) Peperoni\n\t2) Jamón\n\t3) Salmón\n")
    complemento = input("¿Que ingredientes deseas?:  ")
    print("Pizza no vegetarina con mozarrella, tomate y ", complemento)
    if (complemento == "1"):
        print("peperoni")
    elif (complemento == "2"):
        print("jamón")
    else:
        print("salmón")