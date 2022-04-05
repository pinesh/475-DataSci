library("tidyverse")





#read in data
autos<-na.omit(read.csv("auto.csv", header=TRUE))
autos$horsepower <- as.numeric(as.character(autos$horsepower))



#remove missing rows
autos <- autos[complete.cases(autos),]

#part A
#get the mean
summary(autos)

#part B

#range and Sd-------------------------------------
max(autos$mpg)-min(autos$mpg)
sd(autos$mpg)

max(autos$cylinders) - min((autos$cylinders))
sd((autos$cylinders))

max(autos$displacement) - min((autos$displacement))
sd((autos$displacement))

max(autos$horsepower) - min(autos$horsepower)
sd((autos$horsepower))

max(autos$weight) - min(autos$weight)
sd(autos$weight)

max(autos$acceleration) - min((autos$acceleration))
sd(autos$acceleration)

max(autos$year) - min((autos$year))
sd(autos$year)



#part c
#remove 40->80 inclusive
autosC <- autos[-c(39:79),] 

#get the mean
summary(autosC)

#range and Sd-------------------------------------
max(autosC$mpg)-min(autosC$mpg)
sd(autosC$mpg)

max(autosC$cylinders) - min((autosC$cylinders))
sd((autosC$cylinders))

max(autosC$displacement) - min((autosC$displacement))
sd((autosC$displacement))

max(autosC$horsepower) - min(autosC$horsepower)
sd((autosC$horsepower))

max(autosC$weight) - min(autosC$weight)
sd(autosC$weight)

max(autosC$acceleration) - min((autosC$acceleration))
sd(autosC$acceleration)

max(autosC$year) - min((autosC$year))
sd(autosC$year)
#-------------------------------------


#part D
#install.packages("psych")
library(psych)

autos_numeric <- subset(autos, select=-c(name,origin))

pairs.panels(autos_numeric, method = "pearson", density = TRUE, 
             ellipses = TRUE,main = "Significance correlation of auto predictors")



