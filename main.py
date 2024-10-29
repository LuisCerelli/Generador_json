import json

# Función para crear el JSON con los datos de nombre, apellido y edad
def generar_json(nombre, apellido, edad, nombre_archivo):
    # Estructura del JSON
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad
    }
    
    # Guardar el archivo JSON
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(data, archivo, ensure_ascii=False, indent=4)

    print(f"Archivo '{nombre_archivo}' generado correctamente.")

# Solicitar al usuario los datos
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = int(input("Ingrese la edad: "))
nombre_archivo = f"{nombre.lower()}_{apellido.lower()}.json"

# Llamar a la función para crear el archivo JSON
generar_json(nombre, apellido, edad, nombre_archivo)
