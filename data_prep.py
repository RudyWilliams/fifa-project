import pandas as pd
import numpy as np
import eda

df = eda.df
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')

#map countries with less than 100 players into a larger pool
regions = ['South West Asia', 'West Africa', 'East Africa',
           'South Africa (region)', 'Caribbean', 'US-Canada','East Asia - South Pacific',
           'South America', 'Eastern Europe - Russia', 'Europe']

pool = {
    'Afghanistan': regions[0],
    'Albania': regions[-1],
    'Algeria': regions[1],
    'Andorra': regions[-1],
    'Angola': regions[3],
    'Antigua & Barbuda': regions[4],
    'Armenia': regions[0],
    'Azerbaijan': regions[0],
    'Barbados': regions[4],
    'Belarus': regions[-2],
    'Belize': regions[4],
    'Benin': regions[1],
    'Bermuda': regions[4],
    'Bolivia': regions[-3],
    'Bosnia Herzegovina': regions[-1],
    'Botswana': regions[3],
    'Bulgaria': regions[-1],
    'Burkina Faso': regions[1],
    'Burundi': regions[2],
    'Cameroon': regions[1],
    'Canada': regions[5],
    'United States': regions[5],
    'Cape Verde': regions[1],
    'Central African Rep.': regions[2],
    'Chad': regions[2],
    'Comoros': regions[3],
    'Congo': regions[1],
    'Costa Rica': regions[4],
    'Cuba': regions[4],
    'Curacao': regions[4],
    'Cyprus': regions[1],
    'DR Congo': regions[3],
    'Dominican Republic': regions[4],
    'Ecuador': regions[-3],
    'Egypt': regions[2],
    'El Salvador': regions[4],
    'Equatorial Guinea': regions[1],
    'Eritrea': regions[2],
    'Estonia': regions[-2],
    'Ethiopia': regions[2],
    'FYR Macedonia': regions[-1],
    'Faroe Islands': regions[-1],
    'Fiji': regions[6],
    'Finland': regions[-2],
    'Gabon': regions[1],
    'Gambia': regions[1],
    'Georgia': regions[0],
    'Grenada': regions[4],
    'Guam': regions[6],
    'Guatemala': regions[4],
    'Guinea': regions[1],
    'Guinea Bissau': regions[1],
    'Guyana': regions[-3],
    'Haiti': regions[4],
    'Honduras': regions[4],
    'Hong Kong': regions[6],
    'Hungary': regions[-1],
    'Iceland': regions[-1],
    'India': regions[0],
    'Indonesia': regions[6],
    'Iran': regions[0],
    'Iraq': regions[0],
    'Israel': regions[0],
    'Jamaica': regions[4],
    'Jordan': regions[0],
    'Kazakhstan': regions[0],
    'Kenya': regions[2],
    'Korea DPR': regions[6],
    'Kosovo': regions[-1],
    'Kuwait': regions[0],
    'Latvia': regions[-2],
    'Lebanon': regions[0],
    'Liberia': regions[1],
    'Libya': regions[2],
    'Liechtenstein': regions[-1],
    'Lithuania': regions[-2],
    'Luxembourg': regions[-1],
    'Madagascar': regions[3],
    'Mali': regions[1],
    'Malta': regions[-1],
    'Mauritania': regions[1],
    'Mauritius': regions[3],
    'Moldova': regions[-2],
    'Montenegro': regions[-1],
    'Montserrat': regions[4],
    'Morocco': regions[1],
    'Mozambique': regions[3],
    'Namibia': regions[3],
    'New Caledonia': regions[6],
    'New Zealand': regions[6],
    'Nicaragua': regions[4],
    'Niger': regions[1],
    'Northern Ireland': regions[-1],
    'Oman': regions[0],
    'Palestine': regions[0],
    'Panama': regions[4],
    'Paraguay': regions[-3],
    'Peru': regions[-3],
    'Philippines': regions[6],
    'Puerto Rico': regions[4],
    'Qatar': regions[0],
    'Romania': regions[-2],
    'Russia': regions[-2],
    'Rwanda': regions[2],
    'Sierra Leone': regions[1],
    'Slovakia': regions[-1],
    'Slovenia': regions[-1],
    'South Africa': regions[3],
    'South Sudan': regions[2],
    'St Kitts Nevis': regions[4],
    'St Lucia': regions[4],
    'Sudan': regions[2],
    'Suriname': regions[-3],
    'Syria': regions[0],
    #S�o Tom� & Pr�ncipe: regions[],
    'Tanzania': regions[2],
    'Thailand': regions[6],
    'Togo': regions[1],
    'Trinidad & Tobago': regions[4],
    'Tunisia': regions[2],
    'Uganda': regions[2],
    'Ukraine': regions[-2],
    'United Arab Emirates': regions[0],
    'Uzbekistan': regions[0],
    'Venezuela': regions[-3],
    'Zambia': regions[3],
    'Zimbabwe': regions[3],
}

def convert_nationality(nationality):
    return pool[nationality] if nationality in pool.keys() else nationality

#pool smaller nation's players and create new column
df['player_from'] = df['nationality'].apply(convert_nationality)

#cleaning contract_valid_until column
#  first replace nans with 2019
df['contract_valid_until'] = df['contract_valid_until'].fillna(value='2019')
#  next take first four numbers which will be the year
df['contract_valid_until'] = df['contract_valid_until'].apply(lambda x: str(x)[:4])
#  make new field that reflects years left in contract
df['contract_years_left'] = df['contract_valid_until'].astype(int) - 2019

#cleaning height column
def convert_to_inches(h_list):
    if type(h_list) == type(list()):
        return int(h_list[0])*12 + int(h_list[1])
    else:
        return h_list

df['height'] = df['height'].str.split("'") #nans are still there
df['height'] = df['height'].apply(convert_to_inches)

#drop the old columns
df = df.drop(['nationality', 'contract_valid_until'], axis=1)

if __name__ == '__main__':

    #shows that all years are in proper formatt of yyyy and all nans replaced
    # contracts = df.loc[:,['id','contract_valid_until']].groupby('contract_valid_until').count()
    # print(contracts)
    # print(contracts.sum())


    #shows that all years have been replaced
    #comparing with above groupby output, it appears
    #  all 2018->-1, 2019->0, etc
    # years = df.loc[:,['id','contract_years_left']].groupby('contract_years_left').count()
    # print(years)
    # print(years.sum())

    #check height updates
    # print(df.height)
    # heights = df.loc[:,['id','height']].groupby('height').count()
    # print(heights)
    # print(heights.sum() + 48)

    #check that columns have been dropped
    # print(df.info())

    pass