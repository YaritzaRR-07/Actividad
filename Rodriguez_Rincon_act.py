print("Hello")
# Programa Principal de Menú de Opciones, Operaciones, Par o Impar, Saludo, Salir #

print("Hola bienvenidos este Programa de Menú Principal")
print("Escoge una de nuestras siguientes opciones del Menú")


op = ""

while op != "4":
    print("MENÚ PRINCIPAL")
    print("1. Operaciones")
    print("2. Par o Impar")
    print("3. Saludo")
    print("4. Salir")

    op = input("Opcion: ")

    if op == "1":
        sub = ""
        while sub != "3":
            print("SUBMENU OPERACIONES")
            print("1. Sumar 2 numeros")
            print("2. Restar 2 numeros")
            print("3. Volver")

            sub = input("Elige: ")

            if sub == "1":
                a = int(input("A: "))
                b = int(input("B: "))
                print("Resultado:", a + b)

            elif sub == "2":
                print("En esta Opción Te pediremos 2 Números")
                a = int(input("A: "))
                b = int(input("B: "))
                print("Resultado:", a - b)

    elif op == "2":
        sub = ""
        while sub != "2":
            print("SUBMENU PAR O IMPAR")
            print("1. Verificar numero")
            print("2. Volver")

            sub = input("Elige: ")

            if sub == "1":
                print("En esta opción Te pediremos un Número para saber si es PAR o IMPAR ")
                num = int(input("Numero: "))
                if num % 2 == 0:
                    print("Es PAR")
                else:
                    print("Es IMPAR")

    elif op == "3":
        sub = ""
        while sub != "2":
            print("SUBMENU SALUDO")
            print("1. Saludar")
            print("2. Volver")

            sub = input("Elige: ")

            if sub == "1":
                print("En esta Opción te pediremos tu Nombre")
                nombre = input("Tu nombre: ")
                print("Hola", nombre, "bienvenido")

print("SALIR")