from flask import Flask, request, render_template
import tensorflow as tf
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load the models
models = {
    "logistic_regression": joblib.load("LR.pk1"),
    "decision_tree": joblib.load("Decision tree.pk1"),
    "random_forest": joblib.load("Random Forest.pk1"),
    "knn": joblib.load("KNN.pk1"),
    "nn": tf.keras.models.load_model('NN.h5'),
}

# Route to the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', error="No file uploaded")

    file = request.files['file']
    filename = file.filename  # Get the filename
    
    # Validate file format
    if not filename.endswith('.csv'):
        return render_template('index.html', error="Please upload a valid CSV file")

    try:
        # Load CSV into DataFrame
        data = pd.read_csv(file)
    except Exception as e:
        return render_template('index.html', error="Error reading the file: " + str(e))
    
    model_choice = request.form.get('model')
    if model_choice not in models:
        return render_template('index.html', error="Invalid model selected")

    model = models[model_choice]

    # Ensure the CSV has the expected number of columns
    expected_columns = 64  # Replace this with the actual expected column count
    if data.shape[1] != expected_columns:
        return render_template('index.html', error="Invalid CSV structure. Please check the file format (expected number of columns is 64).")

    # Class label mapping (encoded label to original class)
    label_mapping = {
        0: "BENIGN",
        1: "Bot",
        2: "Brute Force",
        3: "DDoS",
        4: "DoS GoldenEye",
        5: "DoS Hulk",
        6: "DoS Slowhttptest",
        7: "DoS slowloris",
        8: "FTP-Patator",
        9: "Heartbleed",
        10: "Infiltration",
        11: "PortScan",
        12: "SSH-Patator",
        13: "Sql Injection",
        14: "XSS"
    }

    if model_choice == "nn":
        # For Neural Network model
        model = models[model_choice]
        predictions = []
        for i, row in data.iterrows():
            prediction = model.predict(row.values.reshape(1, -1))
            original_class = label_mapping.get(np.argmax(prediction[0]), "Unknown Class")
            predictions.append(f"For input number {i+1} in the CSV file, the output is {original_class}")
    else:
        # For other models
        model = models[model_choice]
        predictions = []
        for i, row in data.iterrows():
            prediction = model.predict([row])
            original_class = label_mapping.get(prediction[0], "Unknown Class")
            predictions.append(f"For input number {i+1} in the CSV file, the output is {original_class}")

    # Pass the filename and selected model to the template
    return render_template('index.html', predictions=predictions, filename=filename, model_choice=model_choice)


if __name__ == '__main__':
    app.run(debug=True)
