# Importación de la biblioteca SQLite
import sqlite3

# Establecer una conexión a la base de datos 'mi_base_de_datos.db'
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor, que se utiliza para interactuar con la base de datos
cursor = conn.cursor()

# Crear una tabla 'mensajes' si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mensajes (
        id INTEGER PRIMARY KEY,
        usuario TEXT,
        mensaje TEXT
    )
''')

# Insertar dos registros en la tabla 'mensajes'
cursor.execute("INSERT INTO mensajes (usuario, mensaje) VALUES (?, ?)", ('usuario1', 'Hola, bot!'))
cursor.execute("INSERT INTO mensajes (usuario, mensaje) VALUES (?, ?)", ('usuario2', 'Hola, ¿cómo estás?'))

# Confirmar los cambios en la base de datos
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()

# Reabrir la conexión a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Seleccionar todos los registros de la tabla 'mensajes'
cursor.execute("SELECT * FROM mensajes")
rows = cursor.fetchall()

# Iterar a través de los registros y mostrarlos en la consola
for row in rows:
    print(row)

# Cerrar la conexión a la base de datos nuevamente
conn.close()
