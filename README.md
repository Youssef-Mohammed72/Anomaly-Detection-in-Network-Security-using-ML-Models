# Machine Learning Project

## Overview
This project involves the development, evaluation, and deployment of various machine learning models to classify network traffic data on the (CIC-IDS2017) dataset. The models used include Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Neural Network (NN).

## Project Structure
- `development.py`: Contains the code for data preparation, model training, and evaluation.
- `model_evaluation_metricies.xlsx`: Excel file with the evaluation metrics of the trained models.
- `app.py`: Flask application for deploying the models and making predictions on new data.
- `requirements.txt`: List of dependencies required to run the project.

## Data Preparation
- **Data Loading**: Original datasets are loaded from specified directories.
- **Data Processing**: Data is concatenated, split into training and testing sets, and null values are handled.
- **Feature Scaling**: Data is scaled using `StandardScaler`.
- **Label Encoding**: Labels are encoded using `LabelEncoder`.

## Models
The following models were trained and evaluated:
- **Logistic Regression**
- **Decision Tree**
- **Random Forest**
- **K-Nearest Neighbors (KNN)**
- **Support Vector Machine (SVM)**
- **Neural Network (NN)**

## Evaluation Metrics
The models were evaluated based on the following metrics:
- Accuracy
- Balanced Accuracy
- AUC (Area Under the Curve)
- F1-Score
- Precision
- Recall
- Training Time
- Prediction Time

## Results
The evaluation metrics for each model are summarized in the `model_evaluation_metricies.xlsx` file.

## Deployment
The deployment is done using a Flask web application:
- **Home Route (`/`)**: Renders the home page.
- **Prediction Route (`/predict`)**: Handles file uploads and model predictions.

### Running the Application
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the Flask application:
- python app.py
- Open your web browser and go to http://127.0.0.1:5000/.
- Making Predictions
- Upload a CSV file with the network traffic data.
- Select the model to use for predictions.
- Click the "Predict" button to get the classification results.
## Dependencies
- Python 3.x
- Flask
- TensorFlow
- scikit-learn
- pandas
- numpy
- seaborn
- matplotlib
- joblib
## Dataset
The dataset used in this project is CIC-IDS2017 https://www.unb.ca/cic/datasets/ids-2017.html.
## Acknowledgements
Special thanks to the open-source community for their valuable resources and support.
## Contact
For any questions or feedback, please contact me at youssefmohammed4015@gmail.com.
