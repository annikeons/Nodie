# Importación de bibliotecas
import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

# Inicializar el lematizador de NLTK
lemmatizer = WordNetLemmatizer()

# Cargar las intenciones del chatbot desde un archivo JSON
intents = json.loads(open('chat_bot\intents.json').read())

# Descargar recursos adicionales de NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Listas para almacenar palabras, clases e información de documentos
words = []
classes = []
documents = []
ignore_letters = ['?', '.', ',', '¿', '"', "!"]

# Procesar las intenciones del archivo JSON
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenizar cada patrón en palabras
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # Almacenar el patrón y la etiqueta (intención) en los documentos
        documents.append((word_list, intent["tag"]))
        # Agregar la etiqueta a la lista de clases si no está presente
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# Lematizar palabras y eliminar caracteres ignorados
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
# Ordenar y eliminar duplicados
words = sorted(set(words))

# Guardar las listas de palabras y clases en archivos pickle
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Inicializar listas para datos de entrenamiento
training = []
output_empty = [0] * len(classes)

# Crear datos de entrenamiento en formato bag of words y one-hot encoding
for document in documents:
    bag = [0] * len(words)
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    for word in words:
        if word in word_patterns:
            bag[words.index(word)] = 1

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1

    training.append((bag, output_row))

# Mezclar aleatoriamente los datos de entrenamiento
random.shuffle(training)

# Encontrar la longitud máxima de las bolsas de palabras
max_length = max(len(item[0]) for item in training)

# Asegurarse de que todas las bolsas de palabras tengan la misma longitud
training = [(item[0] + [0] * (max_length - len(item[0])), item[1]) for item in training]

# Convertir los datos de entrenamiento en matrices numpy
train_x = np.array([item[0] for item in training])
train_y = np.array([item[1] for item in training])

# Crear un modelo de red neuronal secuencial
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Definir el optimizador SGD
sgd = SGD(learning_rate=0.001, momentum=0.9, nesterov=True)
# Compilar el modelo con la función de pérdida y métricas
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
# Entrenar el modelo
train_process = model.fit(train_x, train_y, epochs=10, batch_size=5, verbose=1)
# Guardar el modelo entrenado en un archivo
model.save("chatbot_model.h5")
