import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences=["Hello, I love my cat","Hello, I love my dog"]

tk=Tokenizer(num_words=100)
tk.fit_on_texts(sentences)
wordindex=tk.word_index
print(wordindex)