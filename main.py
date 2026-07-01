import numpy as np
import tensorflow as tf 
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

word_index= imdb.get_word_index()
def preprocess_data(input_data):
    words= input_data.lower().split()
    encoded_review = [word_index.get(word,2)+3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review


model = load_model(r'C:\Users\HP\OneDrive\Desktop\RNN-Movie review-Sentiment Alanysis\simple_rnn_imdb.h5')

st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')


##user input
input_data= st.text_area('Movie Review')

if st.button('Classify'):
    processed_input= preprocess_data(input_data)
    #make predictions
    prediction= model.predict(processed_input)
    sentiment= "Positive" if prediction[0][0] > 0.5 else "Negative"

    #display result
    st.write(f"Sentiment: {sentiment}")
    st.write(f"Prediction Score: {prediction[0][0]}")
else:
    st.write("Please enter a movie")


