import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
def process_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens