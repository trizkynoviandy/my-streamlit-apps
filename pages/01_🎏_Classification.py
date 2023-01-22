import joblib
import numpy as np
import PIL
import streamlit as st
import tensorflow as tf

from skimage import transform

st.title("Classification Apps")

option = st.sidebar.selectbox(
     'Select Classification Apps',
     ('-',
      'Diabetes Prediction',
      'Flower Prediction',
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
elif option == "Flower Prediction":
    loaded_model = tf.keras.models.load_model("models/classification/flower_prediction/flower_prediction.h5")
    st.markdown('#### ' + option)
    st.markdown("""
            * Predict the type of flower based on the given image. There are five flowers that this model can predict: daisy, dandelion, roses, sunflowers, and tulips"
            """)
    
    class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
    
    upload= st.file_uploader('Insert image for prediction', type=['png','jpg'])
    c1, c2, c3= st.columns(3)
    if upload is not None:
        np_image = PIL.Image.open(upload)
        np_image = np.array(np_image).astype('float32')/255
        np_image = transform.resize(np_image, (180, 180, 3))
        np_image = np.expand_dims(np_image, axis=0)
        predict = loaded_model.predict(np_image)[0]    
        c1.header('Input Image')
        c2.header('Classes')
        c3.header('Probability')
        c1.image(np_image)
        #c2.subheader({class_names[i]: float(predict[i]) for i in range(5)})
        for i, names in enumerate(class_names):
            c2.write(class_names[i])
            c3.write(f"{predict[i] * 100:.2f} %")
        
        st.subheader(f"The Predicted Class is : :blue[_{class_names[np.argmax(predict)]}_]")

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
            
elif option == "Titanic Survival Prediction":
    
    loaded_model = joblib.load("models/classification/diabetes_prediction/diabetes_prediction_model.sav")
    st.markdown('#### ' + option)
    st.markdown("""
            * Predict whether a person survived the titanic or not
        
            * Dataset source: <https://www.kaggle.com/c/titanic>
            """)
    st.image("https://www.worldhistory.org/img/c/p/1200x627/14047.png")
    
    user_input_1 = st.slider("1. Passenger Class", min_value=1, max_value=3)
    user_input_2 = st.radio("2. Passenger Sex", options=["Male", "Female"])
    user_input_3 = st.slider("3. Passenger Age (Year)", min_value=1, max_value=100)
    user_input_4 = st.number_input("4. SibSp")
    user_input_5 = st.number_input("5. Parch")
    user_input_6 = st.number_input("6. Fare")
    user_input_7 = st.radio("2. Passenger Sex", options=["Cherbourg", "Queenstown", "Southampton"])
    input_data = [[user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6, user_input_7]]

    predict = st.button("Predict")
    
    if predict:
        try:
            prediction = loaded_model.predict(input_data)
            st.success('Prediction Succesful!')
            if str(prediction) == "[0]":
                st.write("Result: NOT SURVIVED")
            else:
                st.write("Result: SURVIVED")
        except ValueError:
            st.write("Make sure you have entered all the required data")
    
else:
    st.write('You selected:', option)