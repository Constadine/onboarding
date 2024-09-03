import matplotlib.pyplot as plt
import json

def plot_sentiment_distribution(input_file):
    with open(input_file, 'r') as f:
        articles = json.load(f)
    
    sentiments = [article['sentiment'] for article in articles]
    
    plt.hist(sentiments, bins=20, color='blue', edgecolor='black')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    plt.show()
