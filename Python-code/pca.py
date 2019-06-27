import pandas as pd 
from sklearn.decomposition import PCA
import eda 

df_subset = eda.df.loc[eda.df['Nationality'].isin(['United States', 'Portugal','Italy','Brasil','England','France','Germany','Mexico']),['ID','Age','Nationality','Finishing','Agility','Stamina','Strength','Marking']]
df_subset = df_subset.dropna(how='any')

avgs = df_subset.groupby('Nationality')[['Age','Finishing','Agility','Stamina','Strength','Marking']].mean()


if __name__ == '__main__':
    df_subset.to_excel('test_subset.xlsx')
    avgs.to_excel('seven_nation_avgs.xlsx')