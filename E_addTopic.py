
import pandas as pd

file = 'data/TimeSegmentation/March_11_15/March_11_15_'

df1 = pd.read_csv(file+'final.csv')
df2 = pd.read_csv(file+'CollectedData_new.csv')
outfile = pd.merge(df1, df2, left_on='tweet_id', right_on='id')
outfile = outfile.drop(['fenci', 'id'], axis=1)
outfile.to_csv(file+'final_new.csv', index=False, encoding='utf-8')


