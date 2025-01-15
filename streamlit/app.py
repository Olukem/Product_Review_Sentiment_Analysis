import streamlit as st
import joblib
from preprocess import preprocess_text  # Import the preprocessing function

# Load the model and TF-IDF vectorizer
model = joblib.load('svc_best_model.joblib')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.joblib')

# Custom header
st.markdown("""
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #8d0801;
        text-align: center;
        margin-bottom: 10px;
        background-image: url('C:/Users/ooluw/Desktop/10nalytics/internship_project/internship_project/images/bi.jpg');
        background-size: cover;
        padding: 50px;
    }
    </style>
    <div class="header">
        Sentiment Analysis on Product Reviews
    </div>
    """, unsafe_allow_html=True)

# Add a logo
st.image("C:/Users/ooluw/Desktop/10nalytics/internship_project/internship_project/images/sa.jpg", width=700)

review = st.text_area("Enter a product review:")

if st.button("Predict Sentiment"):
    if review:
        with st.spinner('Processing...'):
            # Preprocess the input review
            preprocessed_review = preprocess_text(review)
            preprocessed_review_str = ' '.join(preprocessed_review)
            
            # Vectorize the preprocessed review
            vectorized_review = tfidf_vectorizer.transform([preprocessed_review_str])
            
            # Predict the sentiment
            prediction = model.predict(vectorized_review)
            
            # Display the result
            if prediction == 1:
                st.success("The review is positive!")
            else:
                st.error("The review is negative!")
    else:
        st.error("Please enter a review.")

# Custom footer with social media links
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 10px;
    }
    .footer a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    </style>
    <div class="footer">
        Developed by Team Brainiac - ©2024
        <br>
        <a href="https://www.linkedin.com/in/oluwakemi-sorinmade/" target="_blank">LinkedIn</a>
        <a href="https://github.com/Olukem" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)