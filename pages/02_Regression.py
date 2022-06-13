import joblib
import streamlit as st

st.title("Regression Apps")

option = st.sidebar.selectbox(
     'Select Regression Apps',
     ('Personal Insurance Cost',
      'Vehicle Fuel Efficiency'))

if option == "Vehicle Fuel Efficiency":
    
    loaded_model = joblib.load("models/classification/diabetes_prediction/diabetes_prediction_model.sav")
    st.markdown("""
            # Vehicle Fuel Efficiency Prediction
            * Predict vehicle fuel efficiency
            
            * Dataset source: <https://archive.ics.uci.edu/ml/datasets/auto+mpg>
            """)
    
    st.write("1. Cyclinder")
    user_input_1 = st.number_input("Cyclinder")
    st.write("2. displacement")
    user_input_2 = st.number_input("displacement")
    st.write("3. horsepower")
    user_input_3 = st.number_input("horsepower")
    st.write("4. weight")
    user_input_4 = st.number_input("weight")
    st.write("5. acceleration")
    user_input_5 = st.number_input("acceleration")
    st.write("6. model year")
    user_input_6 = st.number_input("model year")
    user_input_7 = st.radio("Origin", ("USA", "Europe", "Japan"))
    input_data = [[user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6, user_input_7]]
    
    predict = st.button("Predict")