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
    'São Tomé & Príncipe': regions[1],
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

#dealing with missing values for 'contract_valid_until' & 'joined'
contract_nans = pd.isna(df['contract_valid_until'])
joined_nans = pd.isna(df['joined'])

df.loc[(contract_nans & joined_nans), ['joined','contract_valid_until']] = '2019'
df.loc[(joined_nans & (~contract_nans)), 'joined'] = (
    df.loc[(joined_nans & (~contract_nans)), 'contract_valid_until'])
df.loc[((~joined_nans) & contract_nans), 'contract_valid_until'] = (
    df.loc[((~joined_nans) & contract_nans), 'joined'])

#cleaning contract_valid_until column
##take first four numbers which will be the year
df['contract_valid_until'] = df['contract_valid_until'].astype(str).apply(lambda x: str(x)[:4]).astype('int')


#cleaning joined column - just take year
df['joined'] = df['joined'].astype(str).apply(lambda x: x[:4]).astype('int')

#consolidate the columns (these are consecutive years with club)
df['years_with_club'] = df['contract_valid_until'] - df['joined'] + 1


#cleaning height column
def convert_to_inches(h_list):
    if type(h_list) == type(list()):
        return int(h_list[0])*12 + int(h_list[1])
    else:
        return h_list

df['height'] = df['height'].str.split("'") #nans are still there
df['height'] = df['height'].apply(convert_to_inches)

#cleaning weight column
def strip_lbs(w_string):
    if type(w_string) == type(''):
        return int(w_string[:-3])
    else:
        return w_string

df['weight'] = df['weight'].apply(strip_lbs)

#drop the old columns
df = df.drop(['nationality','contract_valid_until','joined',
              'real_face','body_type','work_rate'], axis=1)

#strip the money sign and use M or K to determine the factor
def strip_value(value):
    """remove '€' sign unless 0 (otherwise 0 -> nan)"""
    factors = {'M': 1000000, 'K': 1000}
    if value == 0:
        return value
    else:
        value = value.lstrip('€')
        value = float(value[:-1]) * factors[value[-1]]
        return value
        
df['value'] = df['value'].apply(strip_value)
df['wage'] = df['wage'].apply(strip_value)

df['release_clause'] = df['release_clause'].fillna(value=0)
df['release_clause'] = df['release_clause'].apply(strip_value)

if __name__ == '__main__':

    def create_groupby(df,col):
        """use to efficiently create groupbys"""
        return df.loc[:,['id', col]].groupby(col).count()

    # #shows that all years are in proper formatt of yyyy and all nans replaced
    # contracts = create_groupby(df,'contract_valid_until')
    # print(contracts)
    # print(contracts.sum()) # = 18207 => no nans

    # # #check joined column
    # joins = create_groupby(df,'joined')
    # print(joins)
    # print(joins.sum())
  
    # #check new column
    # ywclub = create_groupby(df,'years_with_club')
    # print(ywclub)
    # print(ywclub.sum())

    # print(df.loc[:,['joined','contract_valid_until','years_with_club']])
    ##this spot check shows that the calcutation is working as expected


    #check height updates
    # heights = create_groupby(df, 'height')
    # print(heights)
    # print(heights.sum() + 48) # = 18207 => 48 NaNs
    # #copy paste and place above the cleaning of height: 
    # # print(df.loc[:,['id','height']].groupby('height').count())
    # #comparing the two groupbys is a quick check to see that 
    # #the cleaning went as planned

    #check the weight column
    # weights = create_groupby(df, 'weight')
    # print(weights)
    # print(weights.sum() + 48)
    # #copy paste and place above the cleaning of weight: 
    # # print(df.loc[:,['id','weight']].groupby('weight').count())
    # #comparing the two groupbys is a quick check to see that 
    # #the cleaning went as planned

    #check that columns have been dropped
    # print(df.info())

    #spot checking and everything appears good
    # print(df.loc[df['contract_valid_until']==2018, ['years_with_club','joined','contract_valid_until']])

    #spot checking value/wage
    # print(df['value'])

    #checking release_clause
    # rcs = create_groupby(df, 'release_clause')
    # print(rcs.loc[rcs['id']==58,:])
    # print(rcs.sum()) #see all the nans turned into 0s
    # #spot check looks good

    #checking work_rate
    # wrs = create_groupby(df,'work_rate')
    # print(wrs)
    df = df.drop(['id','name','club','preferred_foot','position','jersey_number'], axis=1)
    grouped = df.groupby('player_from').mean()
    
    #run once
    # grouped.to_excel('data/means_feed_pca.xlsx')

    pass