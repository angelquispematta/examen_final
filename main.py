respuesta = "s"
contar=0
while respuesta == "s":
    diccionario = {"codigo":["1", "2", "3", "4", "5"], "nombre":["azúcar", "arroz", "leche", "atún", "fideos largos"], "precio":["5", "4", "5", "7", "2"]}
    print(diccionario)
    for key in diccionario:
        print(key, ":", diccionario[key])
    codigo = input("Ingresa el código: ")
    cantidad = int(input("Ingresa la cantidad: "))
    if codigo == "e-001":
        precio = 5
        nom_produc_ = "azúcar"
    elif codigo == "e-002":
        precio = 4
        nom_produc_ = "arroz"
    elif codigo =="e-003":
        precio = 5
        nom_produc_ = "leche"
    elif codigo == "e-004":
        precio = 7
        nom_produc_ = "atún"
    elif codigo == "e-005":
        precio = 2
        nom_produc_ = "fideos largos"
    print("El codigo es: ",codigo)
    print("El nombre del producto es :", nom_produc_)
    print("La cantidad es: ",cantidad)
    print("El precio es: ",precio)
    total = precio * cantidad
    print("El monto es: ", total)
    print("Desea continuar Si (s) o No (n)")
    respuesta = input()
    contar += total
print("El precio a pagar es: ",contar)
