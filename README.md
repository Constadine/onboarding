This repository contains a collection of scripts for analyzing news articles. The scripts are organized into the following files:

src/fetch_data.py: This script fetches news articles from a specified API and saves them to a JSON file.
src/preprocess.py: This script preprocesses the fetched news articles by cleaning and normalizing the text data.
src/sentiment.py: This script analyzes the sentiment of the preprocessed news articles and adds sentiment scores to the data.
src/topic_modeling.py: This script performs topic modeling on the preprocessed news articles using Latent Dirichlet Allocation (LDA).
src/visualize.py: This script visualizes the results of the sentiment analysis and topic modeling.
analysis.py: This script orchestrates the entire analysis pipeline, calling each of the above scripts in sequence to fetch, preprocess, analyze, and visualize the news articles.
Usage

To run the analysis pipeline, simply execute the analysis.py script. This will fetch the news articles, preprocess the data, analyze the sentiment, perform topic modeling, and visualize the results.

Dependencies

This repository requires the following dependencies to be installed:

requests for making API requests
json for parsing JSON data
spacy for natural language processing
gensim for topic modeling
matplotlib for visualization

![Sample LDA Visualization](images/lda_visualization.png)

