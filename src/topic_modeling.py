import json
from gensim import corpora, models
from gensim.utils import simple_preprocess
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
import matplotlib.pyplot as plt

def perform_topic_modeling(input_file, num_topics=5):
    with open(input_file, 'r') as f:
        articles = json.load(f)

    # Extract the 'cleaned_text' from each article
    texts = [article['cleaned_text'] for article in articles if article['cleaned_text'].strip()]
    processed_texts = [simple_preprocess(text) for text in texts]

    # Create a dictionary and a corpus
    dictionary = corpora.Dictionary(processed_texts)
    corpus = [dictionary.doc2bow(text) for text in processed_texts]

    # Train the LDA model
    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary)
    
    # Visualize the topics using pyLDAvis
    vis_data = gensimvis.prepare(lda_model, corpus, dictionary)
    pyLDAvis.save_html(vis_data, 'lda.html')

    return lda_model.show_topics()