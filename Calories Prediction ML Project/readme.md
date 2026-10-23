# Calories Prediction ML Project

## Overview
This project is a machine learning application that predicts calories burned based on exercise duration, pulse, and maximum pulse. The project utilizes a linear regression model to make predictions and visualize the results. A Streamlit web interface is provided for interactive usage.

## Packages Used
The following Python packages are used in this project:
- **pandas**: For data manipulation and analysis.
- **scikit-learn**: For building and evaluating the linear regression model.
- **matplotlib**: For visualizing the data and model predictions.
- **numpy**: For numerical operations and array handling.
- **streamlit**: For creating the interactive web interface.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd Calories_prediction_ML
   ```
3. Ensure you have the required libraries installed. You can install them using pip:
   ```
   pip install pandas scikit-learn matplotlib numpy streamlit
   ```
4. Place your dataset in the project directory as `data.csv`.
5. Open `main.ipynb` in Jupyter Notebook or any compatible environment to run the code.
6. To launch the web interface, run the following command in your terminal:
   ```
   streamlit run app.py
   ```

## Usage
- Run the cells in `main.ipynb` to load the data, train the model, and visualize the predictions.
- Use the Streamlit web interface (`app.py`) to interactively input values and view predictions and plots.
- Modify the input values in the prediction section to test different scenarios.

## Additional Information
- The dataset should contain columns for exercise duration, pulse, maximum pulse, and calories burned.
- The notebook and web app include code for data preprocessing, model training, evaluation, and visualization.
- Results and plots will be displayed within the notebook and the web interface for easy interpretation.

## License
This project is licensed under the MIT License.
