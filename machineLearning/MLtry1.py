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
import pyLDAvis
# ---------------------------------------------------------------------------
# INPUTS
# ---------------------------------------------------------------------------

fname = 'testResults/Pubmed_fibrinolysis.csv';
N_ITER = 10;
NUM_TOPIC = 5;

# ---------------------------------------------------------------------------
# SIMULATION ENGINE
# ---------------------------------------------------------------------------

# Read and organising data
data = read(fname);
title = [term[0] for term in data[1:len(data)]];

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

# Generate visualisation
vis_data = pyLDAvis.gensim.prepare(lda,corpus,dictionary)
