#!/usr/bin/env python3

# Hide the annoying depreciation warning in cloudpickle
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

# Imports
import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

# Get the html content of a webpage
topic = "Microsoft"
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/' + topic)
html = response.read()

# Clean up the HTML and get clean text
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)

# Tokenize the HTML
tokens = [t for t in text.split()]

# Remove "stop words"
stop_words = stopwords.words('english')

clean_tokens = tokens[:]
for token in tokens:
    if token.lower() in stop_words:
        clean_tokens.remove(token)

# Count the frequency and plot
freq = nltk.FreqDist(clean_tokens)  
freq.plot(20, cumulative=False)