# Notes on the data_prep.py file

The field names were first converted to lowercase and spaces were replaced with an underscore to make working with the data more comfortable.


### - Pooling smaller nation's players -
The first task was converting 'nationality' to a 'player_from' column. This column grouped countries together that had fewer players. The grouping was done based on regions. The 'nationality' column had no null values to worry about.

### - Cleaning contract_valid_until column -
This column had 289 null values. To deal with these values, I replaced each nan with the current year, '2019'. Since the format for the field was not consistent I converted each to a string and took the first four characters. This would give me the year in the datetime format and just return the same string in the yyyy string format that the other values were in. Looking at the number of contract years left should be better going forward so I created a new column 'contract_years_left' and dropped the 'contract_valid_until' column.

### - Cleaning height column - 
Exploring the data in the eda.py file we see that the data for this column is in the form ft'in. I converted this to be just in inches, switching from a str type to a float. There are 48 nans which I believe will be better to deal with within the player_from groups that will eventually form. 