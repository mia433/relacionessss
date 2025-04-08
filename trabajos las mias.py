opcion=-1
def mostrar ():
        print("aca se ejecuta mostrar")
def agregar():
        print("aca se ejecuta agregar")
def eliminar():
        print("aca se ejecuta eliminar")
def buscar():
        print("aca se ejecuta buscar")
def verificar():
        print("aca se ejecuta verificar")
while (opcion!=6):
        print ("1-Agregar un nuevo estudiante con nombre, edad y materias aprobadas. "
    "2-Mostrar la lista de estudiantes con sus datos. "
    "3-Eliminar un estudiante de la lista por nombre."
    "4-Buscar un estudiante por nombre y mostrar su información."
    "5-Verificar si una palabra clave está en el nombre de algún estudiante.")  
        opcion= int(input(print("ingrese el numero segun lo que quieras solicitar")))
match opcion:
    case 1:
        agregar()
    case 2:
        mostrar()
    case 3:
        eliminar()
    case 4:
        buscar()
    case 5:
        verificar()

estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}

def agregar():
    nombre = input("Introduce el nombre del estudiante: ")
    edad = int(input("Introduce la edad del estudiante: "))
    materias = input("Introduce las materias aprobadas (separar por coma): ").split(",")
    estudiantes[nombre] = {"edad": edad, "materias": [materia.strip() for materia in materias]}
    print(f"Estudiante {nombre} agregado exitosamente.")

def mostrar():
    if estudiantes:
        for nombre, info in estudiantes.items():
            print(f"Nombre: {nombre}, Edad: {info['edad']}, Materias: {', '.join(info['materias'])}")
    else:
        print("No hay estudiantes en la lista.")

def eliminar():
    nombre = input("Introduce el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado exitosamente.")
    else:
        print(f"No se encontró un estudiante con el nombre {nombre}.")

def buscar():
    nombre = input("Introduce el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        info = estudiantes[nombre]
        print(f"Estudiante: {nombre}, Edad: {info['edad']}, Materias: {', '.join(info['materias'])}")
    else:
        print(f"No se encontró un estudiante con el nombre {nombre}.")

def buscarPalabra():
    palabra = input("Introduce una palabra para buscar en los nombres: ")
    encontrados = [nombre for nombre in estudiantes if palabra.lower() in nombre.lower()]
    if encontrados:
        print("Estudiantes encontrados: ", ", ".join(encontrados))
    else:
        print(f"No se encontraron estudiantes con la palabra '{palabra}' en su nombre.")