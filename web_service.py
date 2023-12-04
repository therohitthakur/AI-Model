# Web service using Flask (Python)
from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('text_sentiment_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    # Preprocess the text (tokenization and padding)
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence)

    # Make prediction
    prediction = model.predict(padded_sequence)[0][0]

    # Log prediction in MySQL database (not implemented in this example)

    return jsonify({'text': text, 'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
