# Q3- In Comments, you have a column called comment - Create a wordcloud AFTER cleaning the data properly.

## Pre-processing text data
'''*Text data are cleaned by following below steps.*

- Remove punctuations
- Tokenization - Converting a sentence into list of words
- Remove stopwords
- Lammetization/stemming - Tranforming any form of a word to its root word'''


# Commented out IPython magic to ensure Python compatibility.
# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import nltk 
import string
import re
# %matplotlib inline
pd.set_option('display.max_colwidth', 100)

nltk.download('wordnet')

#loading the excel sheets into notebook
excel_sheets =pd.ExcelFile(r'C:/Users/Abhijeet/Downloads/Tasks/Question Set - FB_Page_Decoder_Data_Analyst.xlsx')

#checking the names of sheets present
excel_sheets.sheet_names

#creating separate dataframes for the sheets

df_posts=excel_sheets.parse('Post_List')
df_comments=excel_sheets.parse('Comments')
df_reactions=excel_sheets.parse('Reactions')
df_shares=excel_sheets.parse('Shares')


string.punctuation

df_comments

comment_df = pd.DataFrame(df_comments[['Name','Comment']])

comment_df

"""## Remove punctuations"""

def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    text = ''.join([c for c in text if ord(c) < 128])
    return text

comment_df['comment_punct'] = comment_df['Comment'].apply(lambda x: remove_punct(str(x)))
comment_df.head(10)

"""## Tokenization"""

def tokenization(text):
    text = re.split('\W+', text)
    return text

comment_df['fb_com_tokenized'] = comment_df['comment_punct'].apply(lambda x: tokenization(x.lower()))
comment_df.head()

"""## Remove stopwords"""

stopword = nltk.corpus.stopwords.words('english')

def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text
    
comment_df['fb_com_nonstop'] = comment_df['fb_com_tokenized'].apply(lambda x: remove_stopwords(x))
comment_df.head(10)

"""## Stemming and Lammitization"""

ps = nltk.PorterStemmer()

def stemming(text):
    text = [ps.stem(word) for word in text]
    return text

comment_df['fb_com_stemmed'] = comment_df['fb_com_nonstop'].apply(lambda x: stemming(x))
comment_df.head()

wn = nltk.WordNetLemmatizer()

def lemmatizer(text):
    text = [wn.lemmatize(word) for word in text]
    return text

comment_df['fb_com_lemmatized'] = comment_df['fb_com_nonstop'].apply(lambda x: lemmatizer(x))
comment_df.head()

# In Comments, you have a column called comment - Create a wordcloud AFTER cleaning the data properly.

#loading required libraries

from wordcloud import WordCloud, STOPWORDS 

import itertools

#creating wordcloud

comment_df_data = comment_df['fb_com_lemmatized']
#print(comment_df_data[0:])

df_data = list(itertools.chain(*comment_df_data[0:]))

text = ' '.join(df_data)
stopwords = set(STOPWORDS)
#stopwords = set(stopwords.words('english'))

wordcloud = WordCloud(collocations=False , width = 1200, height = 1200, background_color ='white', stopwords = stopwords,min_font_size = 10).generate(str(text))
plt.figure(figsize = (12, 12), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()

