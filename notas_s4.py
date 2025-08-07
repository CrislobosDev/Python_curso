# Lista de anotaciones


class Nota:
    def __init__(self, titulo, nota):
        self.titulo = titulo
        self.nota = nota

    def __str__(self):
        return f"{self.titulo} - {self.nota}"


class Libreta:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota agregada {nota}")

    def eliminar_nota(self, titulo):
        for nota in self.notas:
            if nota.titulo.lower() == titulo.lower():
                self.notas.remove(nota)
                print(f"Eliminado: {titulo}")
                return

            print("Nota no encontrada")

    def mostrar_notas(self):
        if self.notas:
            for nota in self.notas:
                print(f" - {nota}")

            return

        print("La libreta esta vacia")


def menu():
    print("** Menu de opciones **")
    print("  1. Agregar nota")
    print("  2. Eliminar nota")
    print("  3. Ver notas")
    print("  4. Salir de la aplicacion")


# Aplicacion
if __name__ == "__main__":
    libreta = Libreta()

    estado = True  # Bandera
    while estado:
        menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                try:
                    titulo = input("Ingrese el titulo de la nota: ")
                    nota = str(input("Ingresa tu nota: "))
                    nota = Nota(titulo, nota)
                    libreta.agregar_nota(nota)
                except ValueError:
                    print("ERROR, Ingrese una nota valida")
            elif opcion == 2:
                titulo = input("Que nota desea eliminar?: ")
                libreta.eliminar_nota(titulo)
            elif opcion == 3:
                libreta.mostrar_notas()
            elif opcion == 4:
                print("Gracias por usar la app")
                estado = False
            else:
                print("Ingrese una opcion valida")
        except ValueError:
            print("** Ingrese una opcion valida ! **")
