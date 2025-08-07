# Lista de anotaciones

class Nota:
    def __init__(self, titulo, nota):
        self.titulo = titulo
        self.nota = nota

class Libreta:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota agregada {nota}")

    def eliminar_nota(self, titulo):
        for nota in self.notas:
            if nota.titulo.lower() == titulo.lower():
                self.titulo.remove(nota)
                print(f"Nota eliminada {titulo}")
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

    estado = True # Bandera
    while estado:
        menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("** Ingrese una opcion valida ! **")

        
        