# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:14:39 2016

@author: ap4409
"""

# ---------------------------------------------------------------------------
# HEADERS
# ---------------------------------------------------------------------------

import sys
sys.path.append('toolbox')
from helpTool import readCSV as read
from nltkExtra import cleanText as clean
import gensim 
# ---------------------------------------------------------------------------
# INPUTS
# ---------------------------------------------------------------------------

fname = 'testResults/Pubmed_fibrinolysis.csv';
N_ITER = 10;
NUM_TOPIC = 10;

# ---------------------------------------------------------------------------
# SIMULATION ENGINE
# ---------------------------------------------------------------------------

# Read and organising data
data = read(fname);
title = [term[1] for term in data[1:len(data)]];

# Cleaning text
textCln = clean(title,'en');

# Bag of words
dictionary = gensim.corpora.Dictionary(textCln)

# Convert tokenized documents into a document-term matrix (bag of words)
corpus = [dictionary.doc2bow(text) for text in textCln]

# Generate LDA model
lda = gensim.models.LdaModel(corpus, num_topics=NUM_TOPIC, id2word = dictionary, passes=N_ITER)

# Print topics
topics = lda.show_topics(NUM_TOPIC)

# Generate visualisation (only for Ipython notebook)
'''
import pyLDAvis.gensim
vis_data = pyLDAvis.gensim.prepare(lda,corpus,dictionary)
pyLDAvis.save_html(vis_data,'LDA_VisualizationLitReview.html')
'''

# Finding main topic for each document
docID = 0;
topic_for_document = {};
for text in corpus:

    currentTopList = lda.get_document_topics(text);
    topic_for_document[docID] = 'N/A'
    
    for currentTop in currentTopList:
        topID = currentTop[0];
        score = currentTop[1];
        
        if score > 0.8:
            topic_for_document[docID] = topID
    
    docID += 1;
    
# Organising documents by topic
classDocuments = {k: [] for k in range(NUM_TOPIC)}
classDocuments['Not Clear Topic'] = [];

for docID in topic_for_document.keys():
    
    if topic_for_document[docID] != 'N/A':
        classDocuments[topic_for_document[docID]].append(title[docID]);
        
    else:
        classDocuments['Not Clear Topic'].append(title[docID])

