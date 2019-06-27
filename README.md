# FIFA Project

Will contain the code and notes for analyzing the FIFA data.

## Contents

### *data*
Contains the data used and generated.
  - data.csv
  - means_feed_pca.xlsx: groupby on player_from and take average for columns
  - nations_lt100.txt: text file containing countries with less than 100 players
  - players.xlsx: file read in initially
  - seven_nation_avgs.xlsx: test data for seeing pca in action
  - test_subset.xlsx: again test data for pca

### *PCA-plots*
Contains the output plots.
  - several plots but same biplot, just zoomed on different regions

### *Python-code*
Contains the Python code. Right now just data cleaning stuff.
  - data_prep.py: code for cleaning the data and groupby and sent to excel
  - eda.py: exploratory to see what needs to be cleaned and how
  - pca.py: can be ignored for now... pca done in R only for now

### *R-models*
Contains the PCA model code written in R.
  - biplot_analysis.md: notes on the initial look at the biplot produced
  - fifa_pca.R: running the pca and producing biplot