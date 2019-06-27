# Notes on the data_prep.py file

The field names were first converted to lowercase and spaces were replaced with an underscore to make working with the data more comfortable. The 48 players missing data for 'height' are missing data for all *skill* fields but still have some data on contracts.


### - Pooling smaller nation's players -
The first task was converting 'nationality' to a 'player_from' column. This column grouped countries together that had fewer players. The grouping was done based on regions. The 'nationality' column had no null values to worry about.

### - Cleaning joined and contract_valid_until columns -
The joined column was missing 1553 values while the contract_valid_until column was missing 289 values. If both columns for a given observation were both nan then I set them both to '2019'. If one column was missing then I copied the value of the other column in its place. This seems to make a reasonable assumption: Players without contract information are probably less valuable players that would have a one-year contract. *Since players may be from a different time, we cannot simply fill nans with a constant value for each observation unless an observation is missing the values in both columns.*

### - Creating years_with_club column -
The creation of this column allows us to get a two-for-one deal; we subtract joined from contract_valid_until and add 1. This gives the number of *consecutive* years with the club. This is likely to be the information we will need going forward rather than the joined and contract_valid_until columns seperately.

### - Cleaning height column - 
Exploring the data in the eda.py file we see that the data for this column is in the form ft'in. I converted this to be just in inches, switching from a str type to a float. There are 48 nans which I believe will be better to deal with within the player_from groups that will eventually form. 

### - Cleaning the weight column
Each entry has the trailing 'lbs' attached to it. Easy enough to clean. Again, the nans remain untouched.

### - Cleaning value and wage column -
There are no nans in these columns. The eda.py file shows that only 0s disobey the expected format of €some_float('M' or 'K'). This is easily cleaned up with the function strip_value() in the module. This converts the two columns from strings to floats.

### - Cleaning release_clause column -
While running the eda.py script we see that release_clause has 1564 nans, and these are the only values violating the expected format (same format as value and wage). We fill these with 0 since not having a release clause amounts to having a release clause of 0. We perform a groupby to see that there are 1564 0s now in release_clauses (i.e. the nans where all transformed properly). The same strip_value()function is applied to the column to clean it.

### - Cleaning work_rate column -
This column has 48 null values. The format is of attacking-work-rate/[space]defending-work-rate. There are three levels for each side: High, Medium, and Low. This totals to 9 possible configs. I just removed this column for now. Information should be captured in the ratings.