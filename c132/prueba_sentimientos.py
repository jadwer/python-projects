import tensorflow.keras
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentence = [
    "I am happy to meet my friends. We are planning to go a party.",
    "I had a bad day at school. i got hurt while playing football",
#    "I had a bad fight with my friend. I think I have even lost sleep",
#    "I started the day confused. My student's father sent me a message"
]

tokenizer = Tokenizer(num_words = 10000, oov_token = '<OOV>')
tokenizer.fit_on_texts(sentence)

word_index = tokenizer.word_index

sequence = tokenizer.texts_to_sequences(sentence)

print(sequence[0:2])

padded = pad_sequences(sequence, maxlen=100, padding="post", truncating="post")

print(padded[0:2])

model = tensorflow.keras.models.load_model("Text_Emotion.h5")

result = model.predict(padded)

print(result)

predict_class = np.argmax(result, axis=1)

encode_emotions = {"anger": 0, "fear": 1, "joy": 2, "love": 3, "sadness": 4, "surprise": 5}
print(encode_emotions)
print(predict_class)