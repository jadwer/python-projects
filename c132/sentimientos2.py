#importamos pandas
import pandas as pd
import tensorflow as tf
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.layers import Conv1D, Dropout, MaxPooling1D


# Leemos el excel y lo guardamos en una variable
train_data_raw = pd.read_excel("Text-Sentiment-Dataset/text-emotion-training-dataset.xlsx")

#imprimimos los 5 primeros datos de nuestro dataframe
print(train_data_raw.head(5))

# Leemos los datos crudos, pero separamos los datos en texto y sentimiento
train_data = pd.DataFrame(train_data_raw["Text_Emotion"].str.split(pat=";", n=1).tolist(), columns = ['Text', 'Emotion'])

#imprimimos los 5 primeros datos de nuestro dataframe
print(train_data.head())

# Imprimimos las emociones diferentes que se encuentren
print("Emociones:", train_data["Emotion"].unique())

#creamos un diccionario de etiqueta : valor
encode_emotions = {"anger": 0, "fear": 1, "joy": 2, "love": 3, "sadness": 4, "surprise": 5}

# reemplazamos los valores de las etiquetas encontradas
train_data.replace(encode_emotions, inplace=True)

#imprimimos el nuevo Dataframe
print(train_data.head())

# Creamos las listas desde el Dataframe

training_sentences = []
training_labels = []

for i in range(len(train_data)) :
    sentence = train_data.loc[i, "Text"]
    training_sentences.append(sentence)

    label = train_data.loc[i, "Emotion"]
    training_labels.append(label)

print("Sentence: ", training_sentences[50], "Label:", training_labels[50])


# tokenización
vocab_size = 10000
embedding_dim = 16
oov_tok = "<OOV>"
training_size = 20000

tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_tok)
tokenizer.fit_on_texts(training_sentences)

# Creamos un ínice de palabras (diccionario)
word_index = tokenizer.word_index

print(word_index["the"])

training_sequences = tokenizer.texts_to_sequences(training_sentences)

print(training_sentences[0], training_sequences[0])
print(training_sentences[1], training_sequences[1])
print(training_sentences[2], training_sequences[2])

# Normalización de datos

padding_type = 'post'
max_length = 100
trunc_type = 'post'

training_padded = pad_sequences(training_sequences, maxlen = max_length, padding=padding_type, truncating = trunc_type)

print(training_padded[0])

training_padded = np.array(training_padded)
training_labels = np.array(training_labels)

print(training_padded)
print(training_labels)

model = tf.keras.Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    Dropout(0.2),

    Conv1D( filters=256, kernel_size = 3, activation = "relu"),
    MaxPooling1D(pool_size = 3),

    Conv1D( filters=128, kernel_size = 3, activation = "relu"),
    MaxPooling1D(pool_size = 3),

    LSTM(128),

    Dense(128, activation = "relu"),
    Dropout(0.2),
    Dense(64, activation="relu"),
    Dense(6, activation="softmax")

])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=['accuracy'])
num_epochs = 100
history = model.fit(training_padded, training_labels, epochs=num_epochs, verbose=2)

model.save("Text_Emotion.h5")