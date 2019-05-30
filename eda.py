import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_excel('players.xlsx')

#164 unique nationalities
# print(len(df['Nationality'].unique()))

df_nans = df.isna()
per_col = df_nans.sum(axis=0)

nationality_counts = df.loc[:,['Nationality','Name']].groupby('Nationality').count()
nationality_counts.columns = ['num_players']
lt100 = nationality_counts.loc[nationality_counts['num_players'] < 100, :]

if __name__ == '__main__':
    
    #run once
    # for i in lt100.index:
    #     with open('nations_lt100.txt', 'a') as f:
    #         f.write(f'{i},{lt100.loc[i,"num_players"]}\n')
    ## those nations will have to be absorbed into a larger pool in the data prep file
    
    #check on nans
    print(per_col)
    ## id, name, age, nationality, overall, potential, ... have no nans
    ## one of the columns needing cleaning is the contract valid until column
    ##  this col has 289 null values

    #check out the height column
    print(df['Height'].isna().sum())
    pass