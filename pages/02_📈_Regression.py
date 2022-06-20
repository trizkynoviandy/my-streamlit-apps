import joblib
import streamlit as st

st.title("Regression Apps")

option = st.sidebar.selectbox(
     'Select Regression Apps',
     ('Personal Insurance Cost',
      'QSAR Fish Toxicity',
      'Vehicle Fuel Efficiency'))

if option == "-":
    st.write("[Please select a classification app]")
elif option == "Personal Insurance Cost":
    st.write("Personal Insurance Cost")
elif option == "QSAR Fish Toxicity":
    loaded_model = joblib.load("models/regression/qsar_fish_toxicity/qsar_fish_toxicity_model.sav")
    st.markdown("#### " + option)
    st.markdown("""
            * Predict acute aquatic toxicity towards the fish Pimephales promelas (fathead minnow)
            
            * Dataset source: <https://archive.ics.uci.edu/ml/datasets/QSAR+fish+toxicity>
            """)
    st.image("https://www.situbiosciences.com/wp-content/uploads/2017/05/fathead-minnow.jpg")
    
    st.write("1. CIC0")
    user_input_1 = st.number_input("CIC0")
    st.write("2. SM1_Dz(Z)")
    user_input_2 = st.number_input("SM1_Dz(Z)")
    st.write("3. GATS1i")
    user_input_3 = st.number_input("GATS1i")
    st.write("4. NdsCH")
    user_input_4 = st.number_input("NdsCH")
    st.write("5. NdssC")
    user_input_5 = st.number_input("NdssC")
    st.write("6. MLOGP")
    user_input_6 = st.number_input("MLOGP")
            
    input_data = [[user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6]]
    predict = st.button("Predict")
    
    if predict:
        try:
            prediction = loaded_model.predict(input_data)
            st.success("Prediction Succesful!")
            st.write(f"Predicted Fish Toxicity: {float(prediction):.3f}")
        except ValueError:
            st.write("Make sure you have entered all the required data")
            
elif option == "Vehicle Fuel Efficiency":
    
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