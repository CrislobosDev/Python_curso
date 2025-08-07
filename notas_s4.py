# Aplicacion de toma de notas
class Nota: # Se crea la clase Nota
    def __init__(self, titulo, nota): # Constructor de la clase Nota 
        self.titulo = titulo # Se inicializa el titulo de la nota
        self.nota = nota # Se inicializa el contenido de la nota

    def __str__(self): # Metodo para representar la nota como una cadena
        return f"{self.titulo} - {self.nota}"


class Libreta: # Clase Libreta que contiene las notas
    def __init__(self):
        self.notas = [] # Inicializa una lista vacia para almacenar las notas

    def agregar_nota(self, nota): # Metodo para agregar una nota a la libreta
        self.notas.append(nota)
        print(f"Nota agregada correctamente: {nota}")

    def eliminar_nota(self, titulo): # Metodo para eliminar una nota por su titulo
        for nota in self.notas: # Recorre la lista de notas
            if nota.titulo.lower() == titulo.lower(): # Compara el titulo de la nota (ignorando mayusculas y minusculas)
                self.notas.remove(nota)
                print(f"Eliminado: {titulo}")
                return

        print("Nota no encontrada")

    def mostrar_notas(self): # Metodo para mostrar todas las notas en la libreta
        if self.notas:
            for nota in self.notas: # Recorre la lista de notas y las imprime
                print(f" -{nota}")

            return

        print("La libreta esta vacia")


def menu(): # Funcion para mostrar el menu de opciones
    print("** MENU DE OPCIONES  **")
    print("     1. Agregar nota")
    print("     2. Eliminar nota")
    print("     3. Ver notas")
    print("     4. Salir de la aplicacion")


# Aplicacion
if __name__ == "__main__": # Punto de entrada de la aplicacion
    libreta = Libreta()  # Crea una instancia de la clase Libreta
    estado = True  # Bandera
    while estado: # Bucle principal de la aplicacion
        menu() # Muestra el menu de opciones
        try: 
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1: # Opcion para agregar una nota recibida por el usuario
                try:
                    titulo = input("Ingrese el titulo de la nota: ") # Solicita el titulo de la nota
                    nota = str(input("Ingresa tu nota: ")) # Solicita el contenido de la nota
                    nota = Nota(titulo, nota) # Crea una instancia de la clase Nota
                    libreta.agregar_nota(nota) # Agrega la nota a la libreta
                except ValueError: # Captura de excepcion si la entrada no es valida
                    print("ERROR, Ingrese una nota valida")
            elif opcion == 2: # Opcion para eliminar una nota
                titulo = input("Que nota desea eliminar?: ") # Solicita el titulo de la nota a eliminar
                libreta.eliminar_nota(titulo) # Elimina la nota de la libreta
            elif opcion == 3: # Opcion para ver todas las notas
                libreta.mostrar_notas() # Muestra todas las notas en la libreta
            elif opcion == 4: # Opcion para salir de la aplicacion
                print("Gracias por usar la app")
                estado = False
            else:
                print("Ingrese una opcion valida")

        except ValueError: # Captura de excepcion si la entrada no es un entero
            print("** Ingrese una opcion valida ! **")
