# input recibe datos del usuario

nombre = input("Ingrese tu nombre: ")
print(f"Hola {nombre}, bienvenido al programa.")

age = input("Ingrese su edad: ")
age = int(age)
print(f"tienes{age} años.")

print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives ? \n").split() # split permite separar los valores ingresados por el usuario

print(f"Vives en {city}, {country}.")
