
import pandas as pd

file = 'data/TimeSegmentation/Feb/Feb'

df1 = pd.read_csv(file+'OriginalData.csv')
df2 = pd.read_csv(file+'CollectedData_doc_topics.csv')
outfile = pd.merge(df1, df2, left_on='tweet_id', right_on='id')
outfile = outfile.drop(['created_at', 'user_id', 'geo_source', 'user_location', 'geo', 'place', 'id', 'location'], axis=1)
outfile.to_csv(file+'final.csv', index=False, encoding='utf-8')