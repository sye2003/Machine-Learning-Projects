import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import streamlit as st

# --- Load and prepare data ---
df = pd.read_csv("data.csv")
df.dropna(inplace=True)

X = df[["Duration", "Pulse", "Maxpulse"]]
y = df["Calories"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# --- Web UI ---
st.title("Calories Burnt Prediction")

duration = st.number_input("Enter Duration (minutes)", min_value=1, max_value=300, value=60)
pulse = st.number_input("Enter Pulse", min_value=40, max_value=200, value=100)
maxpulse = st.number_input("Enter Maxpulse", min_value=50, max_value=250, value=120)

if st.button("Predict Calories"):
    prediction = model.predict([[duration, pulse, maxpulse]])[0]
    st.success(f"Estimated Calories Burnt: {prediction:.2f}")

st.write("Model Accuracy (R² Score):", round(model.score(X_test, y_test), 3))
