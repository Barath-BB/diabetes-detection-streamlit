import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load dataset from URL
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"
]
df = pd.read_csv(url, names=columns)

# App title
st.title('🩺 Diabetes Prediction App')

# Train/test split
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy display
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
st.write(f'**Model Accuracy:** {accuracy:.2f}')

# Sidebar for user input
st.sidebar.header('Enter Patient Data')

def user_input_features():
    return pd.DataFrame({
        'Pregnancies': [st.sidebar.slider('Pregnancies', 0, 17, 1)],
        'Glucose': [st.sidebar.slider('Glucose', 0, 200, 110)],
        'BloodPressure': [st.sidebar.slider('Blood Pressure', 0, 122, 70)],
        'SkinThickness': [st.sidebar.slider('Skin Thickness', 0, 100, 20)],
        'Insulin': [st.sidebar.slider('Insulin', 0, 900, 80)],
        'BMI': [st.sidebar.slider('BMI', 0.0, 70.0, 25.0)],
        'DiabetesPedigreeFunction': [st.sidebar.slider('Diabetes Pedigree Function', 0.0, 2.5, 0.5)],
        'Age': [st.sidebar.slider('Age', 15, 100, 30)]
    })

user_input = user_input_features()

# Display input
st.subheader('Patient Input Data')
st.write(user_input)

# Make prediction
prediction = model.predict(user_input)
st.subheader('Prediction:')
st.write('🧬 **Diabetic**' if prediction[0] == 1 else '✅ **Not Diabetic**')

# Feature importance chart
st.subheader("Feature Importance")
feature_imp = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
st.bar_chart(feature_imp)




