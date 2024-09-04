import spacy
import json

import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading language model for the spaCy 'en_core_web_sm'...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")
    
def preprocess_text(text):
    """
    Preprocess a given text by removing punctuation and stop words,
    and by converting all words to their base form (lemmatization).
    
    Args:
        text (str): The text to preprocess.
    
    Returns:
        str: The preprocessed text.
    """
    # Use the English language model to parse the text
    doc = nlp(text)
    
    # Filter out punctuation and stop words, and lemmatize all words
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    
    # Join the tokens back into a string
    return ' '.join(tokens)

def preprocess_articles(input_file: str, output_file: str) -> None:
    """
    Preprocess a file of articles and save the result.
    
    The preprocessing step is to remove punctuation and stop words, 
    and to convert all words to their base form (lemmatization).
    """
    with open(input_file, 'r') as f:
        articles = json.load(f)
    
    for article in articles:
        # Use the first available field as the text to process
        text = article['title']
        # Preprocess the text
        article['cleaned_text'] = preprocess_text(text)

    # Save processed data
    with open(output_file, 'w') as f:
        json.dump(articles, f)
