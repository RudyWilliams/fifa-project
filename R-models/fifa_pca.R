### Project using PCA on FIFA data

#load in the data
library(readxl)
data <-read_excel("C:/Users/rudyw/DataMining-S19/fifa19/means_feed_pca.xlsx")
dim(data)
data.noids = data[,-1]
ids = data[,1] 
pca = prcomp(data.noids, scale=T)


biplot(pca, scale=T, xlim=c(-0.3,0), ylim=c(-0.175,-0.05))
##shows that a lot of defensive skills are this way like marking,
## standingtackle, slidingtackle, interceptrions, reactions

biplot(pca, scale=T, xlim=c(-0.3,0), ylim=c(-0.05,0))
##see more offensive skills start to show up with loading vectors influncing the 
## first PC

biplot(pca, scale=T, xlim=c(-0.3,0), ylim=c(0, 0.05))
##
##

biplot(pca, scale=T, xlim=c(-0.3,0), ylim=c(0.05,0.175))
##we see acceleration, sprint speed, and agility kind of  
## oppo to defensive skills

biplot(pca, scale=T, xlim=c(0,0.3), ylim=c(-0.25,-0.10))
##the goalkeeper stats
##
