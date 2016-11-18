# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:30:46 2016

@author: Andris Piebalgs

Extract research articles from multiple sources

Science Direct: Max, 200
PubMed : Max, 1000
Google Scholar: No max

Saves results to CSVs and stores results in RAM

"""

import os
import configparser

from googleScholar import googleScholarSearch
from pubmed import pubmedSearch
from science_direct import scienceDirectSearch


# ---------------------------------------------------------------------------
# INPUTS
# ---------------------------------------------------------------------------

search_terms = 'fibrinolysis'
numRes = 100;
saveDir = 'testResults'

# ---------------------------------------------------------------------------
# CHECK
# ---------------------------------------------------------------------------

# Where the API Key is stored
config = configparser.ConfigParser();
config.read('keys.ini')
APIKEY = config['Science Direct']['API Key']

# Checking if file exists, creating one if not
if not os.path.exists(saveDir):
    os.makedirs(saveDir)

# ---------------------------------------------------------------------------
# SIMULATION ENGINE
# ---------------------------------------------------------------------------

print('Retrieving results from Science Direct')
scienceDriectResults = scienceDirectSearch(search_terms,numRes,APIKEY,saveDir);

print('Retrieving results from PubMed')
pubmedResults        = pubmedSearch(search_terms,numRes, saveDir);

print('Retrieving results from Google Scholar')
scholarResults       = googleScholarSearch(search_terms,numRes,saveDir);

# ---------------------------------------------------------------------------
# POST-PROCESSING
# ---------------------------------------------------------------------------










