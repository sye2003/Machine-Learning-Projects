# electricity_app.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("electricity_cost_dataset.csv")
X = df.drop(columns=['structure type', 'electricity cost'])
y = df['electricity cost']

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit App
# Streamlit UI
st.title("Electricity Cost Predictor")

st.write("Enter the details to predict electricity cost:")

# Numeric inputs
site_area = st.number_input("Site Area")
water_consumption = st.number_input("Water Consumption")
recycling_rate = st.number_input("Recycling Rate")
utilisation_rate = st.number_input("Utilisation Rate")
air_quality_index = st.number_input("Air Quality Index")
issue_resolution_time = st.number_input("Issue Resolution Time")
resident_count = st.number_input("Resident Count")

# Structure type dropdown
# structure_type = st.selectbox("Structure Type", df['structure type'].unique())

# Prepare input for prediction
# input_dict = {
#     'site area': site_area,
#     'water consumption': water_consumption,
#     'recycling rate': recycling_rate,
#     'utilisation rate': utilisation_rate,
#     'air qality index': air_quality_index,
#     'issue reolution time': issue_resolution_time,
#     'resident count': resident_count,
# }

# input_df = pd.DataFrame([input_dict])

if st.button("Predict Electricity Cost"):
    prediction = model.predict([[site_area, water_consumption, recycling_rate, utilisation_rate, air_quality_index, issue_resolution_time, resident_count]])[0]
    st.success(f"Predicted Electricity Cost: {prediction:.2f}")


