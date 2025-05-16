import Clientes
from Equipos import Equipo

opciones = 0
cli1 = Clientes.Cliente()

while opciones != 5:
    print("1. Ingresar Cliente")
    print("2. Ver Cliente")
    print("3. Agregar Equipo")
    print("4. Ver equipos por Cliente")
    print("5. Salir")
    print("-*"*25)
    opciones = int(input("Ingrese la opcion que desea: "))

    if opciones == 1:
        apellidos = input("Ingrese apellidos: ")
        nombres = input("Ingrese nombres: ")
        telefono = input("Ingrese teléfono: ")
        cli1.AltasDeCliente(apellidos, nombres, telefono)
    elif opciones == 2:
        print(cli1)
    elif opciones == 3:
        eq = Equipo()
        num_parte = input("Ingrese número de parte: ")
        tipo = input("Ingrese tipo de equipo: ")
        desc = input("Ingrese descripción del problema: ")
        eq.AltaEquipo(num_parte, tipo, desc)
        cli1.AgregarEquipo(eq)
    elif opciones == 4:
        cli1.VerEquipo()
    elif opciones == 5:
        print("Saliendo...")
    else:
        print("Opción inválida, intente de nuevo.")