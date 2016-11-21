# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:11:59 2016
NATURAL LANGUAGE PROCESSING TOOLKIT EXTRA

@author: Andris
"""

from createTokens import preprocess
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

def cleanText(text,lang):
    
    stop = get_stop_words(lang)
    p_stemmer = PorterStemmer()
    
    textCln =[];
    
    for tweet in text:
        
        tokens = preprocess(tweet.lower());    
        
        clnTweet = [];    
        
        for word in tokens:
            
            if word not in stop and len(word) > 2 and not word.startswith('http'):
                
                clnTweet.append((word));
        
        textCln.append(clnTweet)
        
    return textCln

    
    

