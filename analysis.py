import os
# Import custom modules
from src.fetch_data import fetch_articles
from src.preprocess import preprocess_articles
from src.sentiment import add_sentiment_to_articles
from src.topic_modeling import perform_topic_modeling
from src.visualize import plot_sentiment_distribution

# Step 1: Fetch articles
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'category=health&'
       'apiKey=af5d52a7ef3c49dc82424a599a32847d')

output_filename = 'usa_health_articles'
raw_file, articles = fetch_articles(url, output_filename)


# Step 2: Preprocess articles
preprocess_articles(raw_file, f'data/processed/{raw_file}_preprocessed.json')

# Step 3: Perform sentiment analysis
add_sentiment_to_articles(f'data/processed/{raw_file}_preprocessed.json', f'data/processed/{raw_file}_preprocessed_sentiment.json')

# Step 4: Topic modeling
topics = perform_topic_modeling(f'data/processed/{raw_file}_preprocessed_sentiment.json')
print(topics)

# Step 5: Visualize sentiment distribution
plot_sentiment_distribution(f'data/processed/{raw_file}_preprocessed_sentiment.json')

