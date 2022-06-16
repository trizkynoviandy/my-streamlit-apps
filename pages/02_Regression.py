import joblib
import streamlit as st

st.title("Regression Apps")

option = st.sidebar.selectbox(
     'Select Regression Apps',
     ('Personal Insurance Cost',
      'Vehicle Fuel Efficiency'))

if option == "Vehicle Fuel Efficiency":
    
    loaded_model = joblib.load("models/regression/vehicle_fuel_efficiency/vehicle_fuel_efficiency_model.sav")
    st.markdown("""
            # Vehicle Fuel Efficiency Prediction
            * Predict vehicle fuel efficiency
            
            * Dataset source: <https://archive.ics.uci.edu/ml/datasets/auto+mpg>
            """)
    
    st.write("1. Cyclinder")
    user_input_1 = st.number_input("Car cyclinder")
    st.write("2. displacement")
    user_input_2 = st.number_input("Engine displacement")
    st.write("3. horsepower")
    user_input_3 = st.number_input("Car horsepower")
    st.write("4. weight")
    user_input_4 = st.number_input("Car weight")
    st.write("5. acceleration")
    user_input_5 = st.number_input("Car acceleration")
    st.write("6. model year")
    user_input_6 = st.number_input("Model year of manufacture", min_value=int(0), max_value=int(2022))
    st.write("7. Origin")
    user_input_7 = st.radio("Car origin", ("USA", "Europe", "Japan"))
    
    if user_input_7 == "USA":
        user_input_7 = 1
        user_input_8 = 0
        user_input_9 = 0
    elif user_input_7 == "Europe":
        user_input_7 = 0
        user_input_8 = 1
        user_input_9 = 0
    else:
        user_input_7 = 0
        user_input_8 = 0
        user_input_9 = 1
            
    input_data = [[user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6, user_input_7, user_input_8, user_input_9]]
    predict = st.button("Predict")
    
    if predict:
        try:
            prediction = loaded_model.predict(input_data)
            st.success("Prediction Succesful!")
            st.write(f"Predicted Vehicle Fuel Consumption: {float(prediction):.3f} miles per gallon")
        except ValueError:
            st.write("Make sure you have entered all the required data")