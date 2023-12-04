# AI Model using TensorFlow and Keras for sentiment analysis
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample data for training
texts = [
    "And they lived happily ever after.",
    "It was the best of times, it was the worst of times.",
    "They were okay friends, but their friendship kept growing with time."
]

# Labels (1 for positive sentiment, 0 for neutral/negative sentiment)
labels = np.array([1, 1, 0])

# Tokenize and pad sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
total_words = len(tokenizer.word_index) + 1
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences)

# Model definition
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=total_words, output_dim=16, input_length=len(padded_sequences[0])),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Model training
model.fit(padded_sequences, labels, epochs=10)

# Save the trained model
model.save('text_sentiment_model.h5')
