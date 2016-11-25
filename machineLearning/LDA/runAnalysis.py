# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:07:36 2016

@author: ap4409
"""

from LDAFn import *
import pandas as pd
import math

# Read and organising data
data = pd.read_csv('testResults/Pubmed_fibrinolysis.csv')

title = [term[0] for term in data.values];
abstract = [term[1] for term in data.values];

output = analyseText(abstract,10,10);
    
topics = output[0]; # List of main words per topic
blueprint = output[1]; # List of topics for each document (blueprint)

import numpy as np


# Need nicer way to calculate Jensen-Shannon distance

def entropy(prob_dist, base=math.e):
        return -sum([p * math.log(p,base) for p in prob_dist if p != 0])

def jsd(prob_dists, base=math.e):
    weight = 1/len(prob_dists) #all same weight
    js_left = [0,0,0]
    js_right = 0    
    for pd in prob_dists:
        js_left[0] += pd[0]*weight
        js_left[1] += pd[1]*weight
        js_left[2] += pd[2]*weight
        js_right += weight*entropy(pd,base)
    return entropy(js_left)-js_right

testin = 98;
reference = blueprint[testin];

distanceValues = {};

it = 0;
for document in blueprint:
    
    newd = jsd([document,reference])
    distanceValues[newd] = title[it];
    it += 1;

print('Original title is '+ title[testin])

