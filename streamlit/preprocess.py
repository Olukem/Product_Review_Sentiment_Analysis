# preprocess.py
import re
import nltk
import joblib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK data packages are downloaded
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Define the preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters, numbers, and space
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = " ".join(word for word in text.split() if word not in stop_words)
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    text = ' '.join(lemmatizer.lemmatize(word) for word in text.split())
    
    # Tokenization
    text = word_tokenize(text)
    
    return text

# Save the preprocessing function
joblib.dump(preprocess_text, 'preprocess_function.joblib')