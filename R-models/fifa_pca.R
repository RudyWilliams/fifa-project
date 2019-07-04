### Project using PCA on FIFA data

#load in the data
library(readxl)
data <-read_excel("C:/Users/rudyw/DataMining-S19/fifa19/data/means_feed_pca.xlsx")
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


#proportion of variance expained
pcs.vars = pca$sdev^2
pve = pcs.vars/sum(pcs.vars)
pve

plot(pve, type='b', xlab='Principal Component',
     ylab='Proportion of Variance Explained')

plot(c(0,cumsum(pve)), type='b', xlab='Principal Component',
     ylab='Cumulative Proportion of Variance Explained')

#just looking at the principal component scores for each team
z1 = pca$x[,1]
z2 = pca$x[,2]

plot(z1, z2, xlab='First Principal Component', ylab='Second Principal Component',
     type='n', xlim=c(-10,10), ylim=c(-10, 10))
text(z1, z2, labels = seq(1,47))


#k-means clustering on the PCs
set.seed(5)
k3.out = kmeans(pca$x[,c(1,2)], 3, nstart=200)
plot(z1, z2, type='n',
     main='K-Means Clustering on First Two Principal Components',
     xlab='First Principal Component',
     ylab='Second Principal Component')
text(z1, z2, labels=seq(1,47), col=k3.out$cluster+1)

k3.out

#k-means on raw data
set.seed(5)
k3.raw = kmeans(scale(data.noids), 3, nstart=200)

plot(z1, z2, type='n',
     main='K-Means Clustering on Scaled Data',
     sub='(Projected onto PCs for plotting)',
     xlab='First Principal Component',
     ylab='Second Principal Component')
text(z1, z2, labels=seq(1,47), col=k3.raw$cluster+1)
k3.raw

table(true=k3.raw$cluster, predict=k3.out$cluster)

