## The First Biplot
The data was grouped by the player_from column and aggregated by taking the mean of each column. This resulted in a 47x47 dataframe. After running the data through the prcomp() function in R and then creating the biplot we get,\
![initial biplot](https://github.com/RudyWilliams/fifa-project/blob/master/PCA-Plots/pca_initial.png "Initial Biplot") \
The plot is a little hard to read because there are so many predictors (the red arrows). We can zoom in on regions to see what's going on. \
The lower left: \
![lower left](https://github.com/RudyWilliams/fifa-project/blob/master/PCA-Plots/lower_left.png "Lower left of biplot") \
These arrows seem to be mostly of defensive skills like tackling and marking. These loading vectors look to be mostly along the second principal component (I'd like to fix these plots up a bit because they aren't the best). \
The middle left: \
![middle left](https://github.com/RudyWilliams/fifa-project/blob/master/PCA-Plots/middle_left.png "The middle left of biplot") \
We see that as the loading vectors become more horizontal, they seem to be of offensive skills such as shooting and crossing. \
The upper left part 1: \
![upper left 1](https://github.com/RudyWilliams/fifa-project/blob/master/PCA-Plots/top_left1.png "Upper left pt1 of biplot") \
Again, we see the first principal component corresponding to offensive skills. \
The upper left part 2: \
![upper left 2](https://github.com/RudyWilliams/fifa-project/blob/master/PCA-Plots/top_left2.png "Upper left pt2 of biplot") \
The bottom right: \
![bottom right](https://github.com/RudyWilliams/fifa-project/blob/master/PCA-Plots/bottom_right_gk.png "Goalkeeper skills") \
Hard to see still, but these are the goalkeeper skills. Again, this puts the variability of the defensive skills on the second principal component.

