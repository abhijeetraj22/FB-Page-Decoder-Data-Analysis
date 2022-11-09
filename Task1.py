#Q1- Which User is interacting with the page the highest? (Interactions = Likes + Shares + Comments)


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

df_posts.info()

df_comments.info()

df_reactions.info()

df_shares.info()

df_posts.head()

df_comments.head()

df_reactions.head()

df_shares.head()

type(df_posts)

share_inter_page_df = df_shares[df_shares['Page_Or_Person'] == 'Page']
react_inter_page_df = df_reactions[df_reactions['Page_Or_Person'] == 'Page']
comment_inter_page_df = df_comments[df_comments['Page_Or_Person'] == 'Page']

share_inter_page_df.reset_index(drop=True,inplace=True)
react_inter_page_df.reset_index(drop=True,inplace=True)
comment_inter_page_df.reset_index(drop=True,inplace=True)

share_count_df=pd.DataFrame(share_inter_page_df.Shares_By.value_counts())
share_count_df

#repeating the same with other dataframes 

react_count_df=pd.DataFrame(react_inter_page_df.Reactions_By.value_counts())
comment_count_df=pd.DataFrame(comment_inter_page_df.Name.value_counts())

#rename the column
comment_count_df.rename(columns={"Name": "Comments_By"}, inplace=True)

#merging the dataframes to single df for result

total_react=pd.concat([share_count_df,react_count_df,comment_count_df],axis=1, join= 'outer')
total_react['Total_Interactions']=total_react.sum(axis=1)

total_react.replace(np.nan,0,inplace = True)
total_react

#reset & rename the column
total_react.reset_index(inplace=True)
total_react.rename(columns={"index": "User_Name"}, inplace=True)
total_react

#top five User Interaction
top_5 = total_react.sort_values(by=['Total_Interactions'], ascending=False).head(5)
top_5.reset_index(drop=True,inplace=True)

### Generate a Barplot
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(7,5))
plot = sns.barplot(top_5['Total_Interactions'], top_5['User_Name'])
for i,(value,name) in enumerate(zip(top_5['Total_Interactions'],top_5['User_Name'])):
    plot.text(value,i-0.05,f'{value:,.0f}',size=14)
plt.suptitle('Top 5 User Interactions',fontsize = 20)
plt.xlabel("Interaction",fontsize = 20)
plt.ylabel("Users",fontsize = 20)
plt.show();

print("{user_name[0]} user is the most {interact_num[0]} times interacting with the page".format(user_name = top_5['User_Name'],interact_num=top_5['Total_Interactions']))
