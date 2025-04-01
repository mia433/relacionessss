estudiantes={
            "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
            "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
            "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
materias = input("Ingrese las materias aprobadas separadas por comas: ")
estudiantes[nombre] = {"edad": edad, "materias": materias}
print("Estudiante {nombre} agregado correctamente")


if estudiantes:
        for nombre, datos in estudiantes.items():
             print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}")
    else:
        print("No hay estudiantes en la lista.")
    print()