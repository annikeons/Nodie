# Importación de bibliotecas
import random
import json

# Cargar las intenciones del chatbot desde un archivo JSON
intents = json.loads(open('chat_bot/intents.json', encoding='utf-8').read())

# Inicializar un diccionario para almacenar respuestas
responses = {}

# Procesar las intenciones del archivo JSON y mapear patrones a respuestas
for intent in intents['intents']:
    for pattern in intent['patterns']:
        responses[pattern] = intent['responses']

# Mensaje de bienvenida
print("¡Hola! Soy un chatbot. Escribe 'salir' para terminar.")

# Ciclo de interacción con el usuario
while True:
    message = input("Tú: ")  # Capturar el mensaje del usuario
    if message.lower() == 'salir':
        break  # Salir del bucle si el usuario escribe 'salir'
    if message in responses:
        response = random.choice(responses[message])  # Seleccionar una respuesta aleatoria
    else:
        response = "No estoy seguro de cómo responder a eso."  # Mensaje predeterminado si no se encuentra una respuesta
    print(f"Bot: {response}")  # Mostrar la respuesta del bot al usuario

