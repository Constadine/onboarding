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
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

def preprocess_articles(input_file, output_file):
    with open(input_file, 'r') as f:
        articles = json.load(f)
    
    for article in articles:
        article['cleaned_text'] = preprocess_text(article['title'] or article['description'] or '')

    # Save processed data
    with open(output_file, 'w') as f:
        json.dump(articles, f)
