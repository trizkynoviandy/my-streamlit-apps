import joblib
import streamlit as st

st.title("Classification Apps")

option = st.sidebar.selectbox(
     'Select Classification Apps',
     ('Diabetes Prediction',
      'Heart Disease Prediction',
      'Movie Review Sentiment Prediction',
      'Titanic Survival Prediction'))

if option == "Movie Review Sentiment Prediction":
    loaded_model = joblib.load("models/classification/movie_review_model.sav")
    st.markdown('#### ' +   option)
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
else:
    st.write('You selected:', option)