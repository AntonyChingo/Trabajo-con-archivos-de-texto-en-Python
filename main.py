# 1. Crea un nuevo archivo llamado my_notes.txt.
with open("my_notes.txt", "w") as file:
    # 2. Escribe al menos tres líneas de notas personales en el archivo.
    file.write("De lunes a viernes travajo en mecanica y tengo clases de manejo virtual.\n")
    file.write("De sabados a domingos realiso tareas y estudios de la universidad. \n")
    file.write("El tiempo sobrante del domingo dedico a mis jobis.\n")

# 3. Lectura de Archivo de Texto:
# Abre el archivo my_notes.txt.
with open("my_notes.txt", "r") as file:
    # 4. Lee el contenido del archivo línea por línea utilizando el método adecuado.
    lines = file.readlines()

    # 5. Muestra en la consola cada línea leída.
    for line in lines:
        print(line.strip())  # strip() elimina los caracteres de nueva línea al final de cada línea.

