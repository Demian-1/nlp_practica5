import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def lemmatize_token(token):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(token)

def tokenizar(doc):
    if type(doc) != type(""):
        print(doc)
        return ""

    # Tokenize the document
    tokens = word_tokenize(doc, language='spanish')

    # Remove stop words and lemmatize
    stop_words = set(stopwords.words('spanish'))
    filtered_tokens = [lemmatize_token(token) for token in tokens if token.lower() not in stop_words]

    # Join the filtered tokens into a string
    res = " ".join(filtered_tokens)

    return res

# Example usage
text = "Este es un ejemplo de la función de tokenización con NLTK y eliminación de palabras vacías."
result = tokenizar(text)
print(result)
