# Notes on the data_prep.py file

The field names were first converted to lowercase and spaces were replaced with an underscore to make working with the data more comfortable.


### - Pooling smaller nation's players -
The first task was converting 'nationality' to a 'player_from' column. This column grouped countries together that had fewer players. The grouping was done based on regions. The 'nationality' column had no null values to worry about.

### - Cleaning contract_valid_until column -
This column had 289 null values. To deal with these values, I replaced each nan with the current year, '2019'. Since the format for the field was not consistent I converted each to a string and took the first four characters. This would give me the year in the datetime format and just return the same string in the yyyy string format that the other values were in. Looking at the number of contract years left should be better going forward so I created a new column 'contract_years_left' and dropped the 'contract_valid_until' column.