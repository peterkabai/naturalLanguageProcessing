#!/usr/bin/env python3

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

# Imports
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Get the text and tokenize
text = file_get_contents("text_files/harry_potter.txt")
tokens = [t for t in text.split()]

# Generate the wordcloud
wordcloud = WordCloud(background_color="white").generate(text)

# Display the generated image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
