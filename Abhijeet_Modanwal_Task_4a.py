# Q4a - Reshape the Data 
## Using the Reactions Data, Reshape the Data from Long to Wide 
''' - New data will have Columns called Date, Reaction_What , Count of Reactions and Minimum Date to Maximum Dates (*Join Post_List and Reactions to get Date)'''

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

#url_total_count.head()

df_reshape = df_reactions.copy()

df_reshape_data = pd.merge(df_reshape, df_posts, on='Post_URL', how='left')
df_reshape_data.head()

url_total_count.reset_index(inplace=True)
url_total_count.rename(columns={"index": "Post_URL"}, inplace=True)

tlt_reshape_data_df= pd.merge(df_reshape_data, url_total_count, on="Post_URL", how = 'left')
tlt_reshape_data_df.head()

tlt_reshape_data_df.drop(['Post_Text','Post_Embedded_URL','Comment_count','Share_count','Total_reactions'], axis=1,inplace=True)
tlt_reshape_data_df.head()

tlt_reshape_data_df.sort_values(by='post_date',inplace=True)
tlt_reshape_data_df.head()

tlt_reshape_data_df.reset_index(drop=True,inplace=True)
print(tlt_reshape_data_df.head())

tlt_reshape_data_df.dtypes

# saving the dataframe
tlt_reshape_data_df.to_csv(r'Abhijeet_Modanwal_Data.csv', index=False)
