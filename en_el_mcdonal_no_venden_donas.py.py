
def agregar_pendiente(pendientes):
    pendiente = input("Ingrese un nuevo pendiente: ")
    pendientes.append(pendiente)

def mostrar_pendientes(pendientes):
    print("Lista de pendientes:")
    for indice, pendiente in enumerate(pendientes):
        print(f"{indice + 1}. {pendiente}")

def main():
    pendientes = []
    while True:
        print("\n1. agua")
        print("2. luz")
        print("3. gaz")
        opcion = input("hola ")

        if opcion == "1":
            agregar_pendiente(pendientes)
        elif opcion == "2":
            mostrar_pendientes(pendientes)
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()