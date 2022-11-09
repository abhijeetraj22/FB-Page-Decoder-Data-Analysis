# Q2- In Post_List, you have a column called Post_Text - Identify the Keywords on which interactions are the highest. (Interactions = Likes + Shares + Comments)"""

#import required libraries
import numpy as np 
import pandas as pd

#loading the excel sheets into notebook
excel_sheets =pd.ExcelFile(r'C:/Users/Abhijeet/Downloads/Tasks/Question Set - FB_Page_Decoder_Data_Analyst.xlsx')

#checking the names of sheets present
excel_sheets.sheet_names

#creating separate dataframes for the sheets

df_posts=excel_sheets.parse('Post_List')
df_comments=excel_sheets.parse('Comments')
df_reactions=excel_sheets.parse('Reactions')
df_shares=excel_sheets.parse('Shares')



#merging the dataframes to single df for result
url_commt_count=pd.DataFrame(df_comments.Post_URL.value_counts()).rename(columns={'Post_URL':'Comment_count'})
url_react_count=pd.DataFrame(df_reactions.Post_URL.value_counts()).rename(columns={'Post_URL':'Reaction_count'})
url_share_count=pd.DataFrame(df_shares.Post_URL.value_counts()).rename(columns={'Post_URL':'Share_count'})
url_total_count=pd.concat([url_commt_count,url_react_count,url_share_count], axis=1, join= 'outer')
url_total_count['Total_reactions']=url_total_count.sum(axis=1)

url_total_count.head()

#high interaction URL 
url_max_react_count=url_total_count.Total_reactions.idxmax()
url_max_react_count

df_posts.head()

#high interaction post
df_max_react=df_posts.Post_Text.loc[df_posts['Post_URL']==url_max_react_count]

print(df_max_react.iloc[0])

#loading required libraries
#!pip install nltk
#!pip install stop_words

#import required libraries
import nltk
nltk.download("stopwords")
nltk.download('punkt')
from nltk import tokenize
from operator import itemgetter
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

post = df_max_react.iloc[0]

#counting total number of word in post
total_words = post.split()
total_word_length = len(total_words)
print(total_word_length)

#counting number of sentences in post

total_sentences = tokenize.sent_tokenize(post)
total_sent_len = len(total_sentences)
print(total_sent_len)

#calculating tf score

tf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1

# Dividing by total_word_length for each dictionary element
tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())

print(tf_score)

#to know the keyword with hisghest interaction 

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result

print(get_top_n(tf_score,1))
