import joblib
import streamlit as st

st.title("Classification Apps")

option = st.sidebar.selectbox(
     'Select Classification Apps',
     ('-',
      'Diabetes Prediction',
      'Heart Disease Prediction',
      'Movie Review Sentiment Prediction',
      'Titanic Survival Prediction'))

if option == "-":
    st.write("[Please select a classification app]")


elif option == "Movie Review Sentiment Prediction":
    loaded_model = joblib.load("models/classification/movie_review/movie_review_model.sav")
    st.markdown('#### ' + option)
    st.markdown("""
                Predict the sentiment in a movie review
                * This app used logistic regression to train this model, with 91% and 89% accuracy on the training set and the testing set, respectively
                
                * Dataset source: <http://ai.stanford.edu/~amaas/data/sentiment/>
                """)

    text_input = st.text_area(label="Input a movie review", height=250)
    predict = st.button("Predict")

    if predict:
        try:
            prediction = loaded_model.predict(list([text_input]))
            if str(prediction) == "[0]":
                st.success('DONE: This is a negative review')
            else:
                st.success('DONE: This is a positive review')
        except ValueError:
            st.write("Make sure your data is correct")
            
elif option == "Diabetes Prediction":
    
    loaded_model = joblib.load("models/classification/diabetes_prediction/diabetes_prediction_model.sav")
    st.markdown('#### ' + option)
    st.markdown("""
            * Predict whether or not you have diabetes, based on several medical predictor variable
            
            * The predictions obtained by this application have no medical value, to get accurate results please consult a doctor.
            * Dataset source: <https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database>
            """)
    st.image("https://cdn.pixabay.com/photo/2014/11/12/19/25/diabetes-528678_960_720.jpg")
    
    st.write("1. Pregnancies")
    user_input_1 = st.number_input("Number of times pregnant")
    st.write("2. Glucose")
    user_input_2 = st.number_input("Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
    st.write("3. Blood Pressure")
    user_input_3 = st.number_input("Diastolic blood pressure (mm Hg)")
    st.write("4. Skin Thickness")
    user_input_4 = st.number_input("Triceps skin fold thickness (mm)")
    st.write("5. Insulin")
    user_input_5 = st.number_input("2-Hour serum insulin (mu U/ml)")
    st.write("6. Body Mass Index")
    user_input_6 = st.number_input("Body mass index (weight in kg/(height in m)^2)")
    st.write("7. Diabetes Pedigree Function")
    user_input_7 = st.number_input("Diabetes pedigree function")
    st.write("8. Age")
    user_input_8 = st.number_input("Age (years)")
    input_data = [[user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6, user_input_7, user_input_8]]

    predict = st.button("Predict")
    
    if predict:
        try:
            prediction = loaded_model.predict(input_data)
            st.success('Prediction Succesful!')
            if str(prediction) == "[0]":
                st.write("Result: NEGATIVE")
            else:
                st.write("Result: POSITIVE")
        except ValueError:
            st.write("Make sure you have entered all the required data")
    
else:
    st.write('You selected:', option)