from textblob import TextBlob
import json
def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

def add_sentiment_to_articles(input_filename, output_filename):
    """
    Add sentiment to a file of articles and save the result.
    """
    with open(input_filename, 'r') as input_file:
        articles = json.load(input_file)
    
    for article in articles:
        article['sentiment'] = analyze_sentiment(article['cleaned_text'])
    
    # Save sentiment-analyzed data
    with open(output_filename, 'w') as output_file:
        json.dump(articles, output_file)
