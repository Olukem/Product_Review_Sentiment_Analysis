# Product_Review_Sentiment_Analysis

## Demo
<video src= "https://github.com/Olukem/Product_Review_Sentiment_Analysis/raw/main/demo.mp4" controls>
</video>

<video src="https://github.com/Olukem/Product_Review_Sentiment_Analysis/raw/main/Demo.mp4" controls width="720">
</video>

# Overview
In today's e-commerce landscape, analyzing customer feedback is crucial for businesses to make data-driven decisions. This project focuses on building an end-to-end sentiment analysis solution for customer review for our business stakeholers. By leveraging Data Science and Machine Learning techniques, the project aims to preprocess, analyze, and visualize customer sentiments from textual reviews. A successful sentiment analysis implementation will significantly enhance customer trust and business growth..

# Problem Statement
In the digital age, e-commerce platforms like Amazon handle vast amounts of customer feedback. Manually analyzing thousands of product reviews is time-consuming and inefficient.  Manually analyzing these reviews is inefficient and time-consuming. The goal of this project is to develop an automated sentiment analysis system that can process and interpret these reviews to provide insights into customer satisfaction and areas of improvement.

# Project Objectives
1.  Develop an end-to-end sentiment analysis system for e-commerce product reviews in the Electronics category.
2.  Extract, preprocess, analyze, and visualize customer sentiment from textual reviews.
3.  Provide actionable insights to stakeholders to improve customer satisfaction, product development, and marketing strategies.

# Technologies Used
    Programming Language: Python
    Libraries/Frameworks:
        Data Handling: numpy, pandas
        Data Visualization: matplotlib, seaborn
        Natural Language Processing: nltk, re
        Machine Learning: sklearn (including train_test_split, MultinomialNB, LogisticRegression,      RandomForestClassifier, SVC)
        Sentiment Analysis Pre-trained Models: VADER, TextBlob
        Web Framework: Streamlit
        Feature Extraction: CountVectorizer, TfidfVectorizer
        Word Cloud Generation: wordcloud

# Features
1.   Text Preprocessing:
       Case normalization, tokenization, lemmatization, and removal of noise (e.g., special characters, stopwords).
2.  Feature Engineering:
       Bag of Words (BoW) and Term Frequency-Inverse Document Frequency (TF-IDF) methods.
3.  Machine Learning Models:
       Custom Models: Naive Bayes, Logistic Regression, Random Forest, and SVC.
       Pre-trained Models: VADER and TextBlob.
4.  Performance Evaluation:
       Metrics include Accuracy, Precision, Recall, and F1 Score.
5.  Deployment:
       streamlit local deployment for real-time sentiment analysis.

# How to Run the Project
1. Clone the repository:
  git clone https://github.com/Olukem/Product_Review_Sentiment_Analysis.git

    cd customer-sentiment-analysis

3. Install the required dependencies:
   pip install -r requirements.txt

4. Run Jupyter Notebooks for Analysis:
    Open the notebooks/ folder.

5. Run the Streamlit App:
  For Streamlit:
    streamlit run app.py

6. Input Review Text: Once the app is running, input a review for sentiment analysis and get instant predictions.


# Key Findings
    The Naive Bayes model achieved an accuracy of 97.47% and an F1 score of 97.20%.


# Results and Findings
The Random Forest model performed the best, achieving an accuracy of 99.17%. However, Naive Bayes is preferred for its simplicity and ease of deployment, offering competitive results. The insights gained from sentiment analysis can inform customer service strategies and product development.

# Model Deployment
The model is deployed using Streamlit. Users can input a review text, and the model will predict whether the sentiment is positive, negative, or neutral. The web application provides an easy interface for real-time sentiment predictions.

# Limitations
    Struggles with sarcasm or ambiguous language.
    Limited scope (only Electronics category reviews).
    Performance may degrade without frequent updates to the sentiment lexicon.

# Next Steps
    Improve the model’s ability to handle sarcasm and ambiguous language.
    Integrate additional datasets for broader coverage and improve robustness.
    Continuously update the sentiment lexicon to adapt to changing trends in language.

# Conclusion
  The sentiment analysis system developed successfully processes product reviews. The results from the project will help inform product development and improve customer satisfaction.

# Future Recommendations

    Explore methods for better handling sarcasm and ambiguous reviews.
    The integration of additional data sources to make the model more generalizable.

