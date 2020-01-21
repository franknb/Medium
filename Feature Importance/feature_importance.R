library(ranger)
library(datasets)
data(iris)

# Creating ranger models and count runtime
t0 <- Sys.time()
rg1 <- ranger(Species~., data = iris, importance = "impurity")
t1 <- Sys.time()
rg2 <- ranger(Species~., data = iris, importance = "impurity_corrected")
t2 <- Sys.time()
rg3 <- ranger(Species~., data = iris, importance = "permutation")
t3 <- Sys.time()

# Prepare for plotting
df <- data.frame("Feature" = names(rg1$variable.importance),
                 "Gini.importance" = rg1$variable.importance,
                 "AIR.importance" = rg2$variable.importance,
                 "Permutation.importance" = rg3$variable.importance)
# Plotting
par(mfrow=c(1,3))
par(mar=c(5,6,4,0)+.1)
p1 <- barplot(df$Gini.importance, horiz=TRUE, names.arg = df$Feature, las=2, xlab = "Gini importance", col = 'beige')
legend("bottomright",inset=-.025,legend =paste("runtime",round(t1-t0,2),"s"), bty = "n")
text(0, p1, round(df$Gini.importance,2),cex=1,pos=4) 
par(mar=c(5,3,4,3)+.1)
p2 <- barplot(df$AIR.importance, horiz=TRUE, las=2, xlab = "AIR importance", col = 'beige')
legend("bottomright",inset=-.025,legend =paste("runtime",round(t2-t1,2),"s"), bty = "n")
text(0, p2, round(df$AIR.importance,2),cex=1,pos=4) 
par(mar=c(5,1,4,5)+.1)
p3 <- barplot(df$Permutation.importance, horiz=TRUE, las=2, xlab = "Permutation importance", col = 'beige')
legend("bottomright",inset=-.025,legend =paste("runtime",round(t3-t2,2),"s"), bty = "n")
text(0, p2, round(df$Permutation.importance,2),cex=1,pos=4) 

