# Generador de Archivos JSON de Datos Personales

Este script permite crear un archivo JSON que contiene datos personales básicos, como el nombre, el apellido y la edad del usuario. La información se guarda en un archivo cuyo nombre se genera a partir del nombre y apellido ingresados, proporcionando una estructura ordenada y de fácil acceso en formato JSON.

## Descripción del Funcionamiento

El script solicita al usuario los siguientes datos:
1. **Nombre**
2. **Apellido**
3. **Edad**

A continuación, genera un archivo JSON con una estructura clara que almacena estos datos, utilizando el formato `nombre_apellido.json` como nombre de archivo. Los datos son guardados en español y con una indentación adecuada para facilitar la lectura.

### Ejemplo de Uso

Supongamos que el usuario ingresa los siguientes datos:
- Nombre: Juan
- Apellido: Pérez
- Edad: 30

El programa generará un archivo llamado `juan_pérez.json` con el siguiente contenido:

```json
{
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30
}
```

### **Utilidad en Ingeniería de Datos**

**Este código es útil en Ingeniería de Datos ya que permite estandarizar y estructurar información en formato JSON, facilitando su integración en pipelines de datos y su uso en sistemas que dependen de formatos de datos estructurados.** Al ser JSON un formato ampliamente utilizado en APIs y almacenamiento de datos, esta herramienta puede aplicarse en tareas de ETL (extracción, transformación y carga de datos) y en la generación de archivos para transferencia de datos entre diferentes sistemas.

## Consideraciones

- Asegúrate de que tienes permisos de escritura en el directorio donde se ejecuta el script, ya que el archivo JSON se guardará en esa ubicación.
- El archivo JSON se sobrescribirá si se vuelve a ejecutar el programa con los mismos datos.
- Al ser un archivo de texto, el JSON puede abrirse con cualquier editor de texto, pero para una visualización más cómoda, se recomienda utilizar un editor compatible con JSON.

## Requisitos

Este script está escrito en Python 3 y no requiere librerías adicionales más allá de las estándar.

