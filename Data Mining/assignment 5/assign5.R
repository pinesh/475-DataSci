#Harry Pines Assignment 5

#' 1) 

library("tidyverse")
library(dplyr)

#read in data

autos<-na.omit(read.csv("Auto.csv", header=TRUE))
suppressWarnings(autos$horsepower <- as.numeric(as.character(autos$horsepower)))
autos <- autos[complete.cases(autos),]

#' a. (5%) Perform a multiple linear regression with mpg as the response 
#' and all other variables except name as the predictors. 
input = subset(autos, select=-c(name))
print(head(input))

# Build the model
model <- lm(mpg~cylinders+displacement+horsepower+weight+acceleration+year+origin,
            data = input)

# Show the model.
summary(model)

#the summary indicates that we have several strong predictors 
#in the 99.9% confidence interval. 

#'i) Which predictors appear to have a statistically significant relationship 
#'to the response, and how do you determine this?

#Based on the p values, the strongest predictors
#of miles to the gallon are the weight, year and origin

#'ii) What does the coefficient for the displacement 
#'variable suggest, in simple terms?

# The coefficient of the variable displacement is estimated to be approx 0.01,
# this is the multiplier applied to the variable in the prediction. 
# The p value indicates a value < 0.01 which implies 
# statistical significance at a 99% confidence level.   

#' b. (5%) Produce diagnostic plots of the linear regression fit. 

par(mfrow=c(2,2)) # Change the panel layout to 2 x 2
plot(model)
par(mfrow=c(1,1)) # Change back to 1 x 1

#the residual plot appears to be good. the data is
#distributed around a relatively horizontal line without many outliers.
# the normal Q-Q also appears to be linear and the scale location is permissible.
# there are seemingly no cases directly beyond the cooks distance line, 


#'c. (5%) Fit linear regression models with interaction effects.
#'

#interactions between cylinders and displacement
# Build the model
model2 <- lm(mpg~cylinders*displacement+horsepower+weight+acceleration+year+origin,
             data = input)

# Show the model
summary(model2)

#with a lower standard of error and higher statistical significance 
#across the board, there is likely an interaction relationship 
#between cylinders and displacement.
par(mfrow=c(2,2)) # Change the panel layout to 2 x 2
plot(model2)
par(mfrow=c(1,1)) # Change back to 1 x 1


#interactions between weight and horsepower
# Build the model
model3 <- lm(mpg~cylinders+displacement+horsepower*weight+acceleration+year+origin,
             data = input)

# Show the model
summary(model3)

par(mfrow=c(2,2)) # Change the panel layout to 2 x 2
plot(model3)
par(mfrow=c(1,1)) # Change back to 1 x 1

#the r2 value indicates this model is also better than one without any 
#interactions



#interactions between weight and year
# Build the model
model4 <- lm(mpg~cylinders+displacement+horsepower+weight*year+acceleration+origin,
             data = input)

# Show the model
summary(model4)

par(mfrow=c(2,2)) # Change the panel layout to 2 x 2
plot(model4)
par(mfrow=c(1,1)) # Change back to 1 x 1

#the r2 value indicates this model isn't vastly different from the initial model.
#there likely isn't a strong relationship


#'2) This problem involves the Boston data set, which we saw in class. We will now try to predict
#' per capita crime rate using the other variables in this data set. In other words, per capita
#' crime rate is the response, and the other variables are the predictors.


boston<-na.omit(read.csv("HousingData.csv", header=TRUE))
boston <- boston[complete.cases(boston),]
summary(boston)


#' a. (6%) For each predictor, fit a simple linear regression model to predict the response.
#' Include the code, but not the output for all models in your solution.

boston.crime.lm.ZN <- lm(CRIM ~ ZN,data = boston)
summary(boston.crime.lm.ZN)

boston.crime.lm.INDUS <- lm(CRIM ~ INDUS,data = boston)
#summary(boston.crime.lm.INDUS)

boston.crime.lm.CHAS <- lm(CRIM ~ CHAS,data = boston)
#summary(boston.crime.lm.CHAS)

boston.crime.lm.NOX <- lm(CRIM ~ NOX,data = boston)
#summary(boston.crime.lm.NOX)

boston.crime.lm.RM <- lm(CRIM ~ RM,data = boston)
#summary(boston.crime.lm.RM)

boston.crime.lm.AGE <- lm(CRIM ~ AGE,data = boston)
#summary(boston.crime.lm.AGE)

boston.crime.lm.DIS <- lm(CRIM ~ DIS,data = boston)
#summary(boston.crime.lm.DIS)

boston.crime.lm.RAD <- lm(CRIM ~ RAD,data = boston)
#summary(boston.crime.lm.RAD)

boston.crime.lm.TAX <- lm(CRIM ~ TAX,data = boston)
#summary(boston.crime.lm.TAX)

boston.crime.lm.PTRATIO <- lm(CRIM ~ PTRATIO,data = boston)
#summary(boston.crime.lm.PTRATIO)

boston.crime.lm.B <- lm(CRIM ~ B,data = boston)
#summary(boston.crime.lm.B)

boston.crime.lm.LSTAT <- lm(CRIM ~ LSTAT,data = boston)
#summary(boston.crime.lm.LSTAT)


boston.crime.lm.MEDV <- lm(CRIM ~ MEDV,data = boston)
#summary(boston.crime.lm.MEDV)


#' b. (6%)

#for each model, all were significant with the exception of CHAS.

#The variable meanings are defined as follows:
#CRIM - per capita crime rate by town

#NOX - nitric oxides concentration (parts per 10 million)
boston.graph.NOX<-ggplot(boston, aes(x=NOX, y=CRIM))+
  geom_point()
boston.graph.NOX <- boston.graph.NOX + geom_smooth(method="lm", col="black")

boston.graph.NOX
#Here, the relationship appears to be linearly increasing.


#CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
boston.graph.CHAS<-ggplot(boston, aes(x=CHAS, y=CRIM))+
  geom_point()
boston.graph.CHAS <- boston.graph.CHAS + geom_smooth(method="lm", col="black")
boston.graph.CHAS

#here the relationship indicates crime is more prevalent away from the river

#MEDV - Median value of owner-occupied homes in $1000's
boston.graph.MEDV<-ggplot(boston, aes(x=MEDV, y=CRIM))+
  geom_point()

boston.graph.MEDV <- boston.graph.MEDV + geom_smooth(method="lm", col="black")
boston.graph.MEDV
#Here, the relationship appears to be linearly decreasing.


#DIS - weighted distances to five Boston employment centres.
boston.graph.DIS<-ggplot(boston, aes(x=DIS, y=CRIM))+
  geom_point()

boston.graph.DIS <- boston.graph.DIS + geom_smooth(method="lm", col="black")
boston.graph.DIS

#Here, the relationship appears to be linearly decreasing.


#'c. (6%) 

model5 <- lm(CRIM~ZN+INDUS+CHAS+NOX+RM+AGE+DIS+RAD+TAX+PTRATIO+B+LSTAT+MEDV,
             data = boston)
summary(model5)
#examining all of them together suggests the most significant predictor is RAD,
#followed by DIS and MEDV. 

#we can reject the null hypothesis for RAD,DIS,MEDV and ZN.
#NOX and B both have >90% certainty but that's outside our 95% field.

par(mfrow=c(2,2)) # Change the panel layout to 2 x 2
plot(model5)
par(mfrow=c(1,1)) # Change back to 1 x 1

#with the highest R2 value, this model is the better predictor when compared 
#to the individual models.


#'d. (6%)  What does this plot tell you about the various predictors?

#build the coefficient table,
name <- colnames(boston)[2:14]
univ <- c(coef(summary(boston.crime.lm.ZN))["ZN","Pr(>|t|)"],
coef(summary(boston.crime.lm.INDUS))["INDUS","Pr(>|t|)"],
coef(summary(boston.crime.lm.CHAS))["CHAS","Pr(>|t|)"],
coef(summary(boston.crime.lm.NOX))["NOX","Pr(>|t|)"],
coef(summary(boston.crime.lm.RM))["RM","Pr(>|t|)"],
coef(summary(boston.crime.lm.AGE))["AGE","Pr(>|t|)"],
coef(summary(boston.crime.lm.DIS))["DIS","Pr(>|t|)"],
coef(summary(boston.crime.lm.RAD))["RAD","Pr(>|t|)"],
coef(summary(boston.crime.lm.TAX))["TAX","Pr(>|t|)"],
coef(summary(boston.crime.lm.PTRATIO))["PTRATIO","Pr(>|t|)"],
coef(summary(boston.crime.lm.B))["B","Pr(>|t|)"],
coef(summary(boston.crime.lm.LSTAT))["LSTAT","Pr(>|t|)"],
coef(summary(boston.crime.lm.MEDV))["MEDV","Pr(>|t|)"])
coef_table <- data.frame(name,univ)

coef_table$multi <- model5$coefficients[2:14]


plot(coef_table$univ,coef_table$multi, 
     main = "Univariate vs. Multiple Regression ",
     xlab = "Univariate", ylab = "Multiple")

#the table suggests two of the predictors differ extensively compared 
#to the others across comparisons

#'   e. (6%) Is there evidence of non-linear association between any of 
#'   the predictors and the
#' response?

#' Hint: use the poly() function in R. Again, include the code, 
#' but not the output for
#' each model in your solution, and instead describe any non-linear trends you
#' uncover.
deterfit <- function(column) {
  fit_1 = lm(CRIM~column, data = boston)
  fit_2 = lm(CRIM~poly(column,2), data = boston)
  fit_3 = lm(CRIM~poly(column,3), data = boston)
  fit_4 = lm(CRIM~poly(column,4), data = boston)
  fit_5 = lm(CRIM~poly(column,5), data = boston)
  print(anova(fit_1,fit_2,fit_3,fit_4,fit_5))
}

deterfit(boston$ZN)
#the poly determinate of ZN indicates that a nonlinear association 
#would be more suitable

deterfit(boston$INDUS)
#the poly determinate of INDUS suggests a quartic polynomial would be best

#Chas is a dummy variable and thus has no linear fit.

#deterfit(boston$NOX)
#the poly determinate of NOX suggests a quartic polynomial would be best

#deterfit(boston$RM)
#the poly determinate of RM suggests a cubic polynomial would be best

#deterfit(boston$AGE)
#the poly determinate of age suggests a quartic polynomial would be best

#deterfit(boston$DIS)
#the poly determinate of DIS suggests a quintic polynomial would be best but
#the true fit likley is beyond 6

#deterfit(boston$RAD)
#the poly determinate of RAD suggests a cubic polynomial would be best

#deterfit(boston$TAX)
#the poly determinate of TAX suggests a square polynomial would be best

#deterfit(boston$PTRATIO)
#the poly determinate of PRATIO suggests linear is appropriate

#deterfit(boston$B)
#the poly determinate of B suggests linear is appropriate

#deterfit(boston$LSTAT)
#the poly determinate of lstat suggests a square polynomial would be best

#deterfit(boston$MEDV)
#the poly determinate of MEDV suggests quintic polynomial would be best


#' 3) Suppose we collect data for a group of students in a 
#' statistics class with variables:

#'a. (5%) Estimate the probability that a student who studies for 32 h, has 
#'a PSQI score of 12
#'and has an undergrad GPA of 3.0 gets an A in the class. Show your work.

#PREDICTION -> y = -7 + 0.1(hours) + 1(undergradgpa) + -0.04(pSQI)
a_predict <- -7 + (0.1*32) + 1*3 + (-0.04*12)
a_predict

#since its less than 0, the prediction would indicate the probability is 0.


#'b. (5%) How many hours would the student in part 
#'(a) need to study to have a 50 % chance of getting an A in the class? 

#if y = 0.5,  0.5 = -7 + (0.1*x) + 3 + (-0.04*12)
# 7.5 = 0.1x + 3 -0.48
# 4.5 = 0.1x -0.48
# 4.98 = 0.1x
# 49.8 = x

#thus the student would need to study for 49.8 hours.

#'c. (5%) 
#if y = 0.5,  0.5 = -7 + (0.1*x) + 3 + (-0.04*3)
# 7.5 = 0.1x + 3 
# 4.5 = 0.1x -0.12
# 4.62 = 0.1x
# 46.2 = x

#thus the student would need to study for 46.2 hours.
       
#'4) 
library("tm")

library("SnowballC")
originaldataset = read.csv("GuardianArticles.csv",stringsAsFactors = FALSE)

# Load the data
docs <- VCorpus(VectorSource(originaldataset$body))
#docs <- Corpus(VectorSource(text))

# Convert the text to lower case, removing whitespace, stopwords, punctuation and
#setting it all to lowercase
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, stemDocument)



dtm <- TermDocumentMatrix(docs)
dtm = removeSparseTerms(dtm, 0.99)
m <- as.matrix(dtm)

#'a. Tokenization (20%)


print(originaldataset$body[10])
chosenrow <-(m[,10])
chosenrow[which(chosenrow==0)] = NA_character_
demo <- data.frame(chosenrow)
demo <- demo[complete.cases(demo),]
print(demo)


#'b. Classification (20%)


library("tidyverse")
library(dplyr)
# Loading package 
library(e1071) 
library(caTools) 
library(caret) 
article_type <- recode(originaldataset$section, 'culture'=0, 
                       'sport'=1, 'technology'=2, 'world'=3,
                       'artanddesign'=4,'business'=5,.default = 7)

max(article_type)

features <- t(m)

correlationMatrix <- cor(features)

highlyCorrelated <- findCorrelation(correlationMatrix, cutoff=0.75)

features <- t(m)  
features <- features[,-highlyCorrelated]
feature_set <- cbind(features,article_type)  

df = as.data.frame(feature_set)
df <- as.data.frame(feature_set)

fit = glm(article_type ~.,family ="gaussian",data = df)
  temp <- varImp(fit)
library(dplyr)
n <- as.data.frame(temp)

#keep the top 80.0198 by importance%
n_sorted <- head(arrange(n,desc(Overall)),2000)
names <- colnames(t(n_sorted))

#somehow we lost some
names <- names[-622]
print(names[1625])
names <- names[-1625]
print(names[1645])
names <- names[-1645]
output <- df[, names[1:1997]]

#re-attach the feature sets
#make it binary
output[output > 0] <- 1
output <- cbind(output,article_type)  
output$article_type <- as.factor(output$article_type)
set.seed(1234) 

samp <- createDataPartition(output[,1], p = 0.8, list = FALSE)
training <- output[samp,]
testing <- output[-samp,]

classifier <- naiveBayes(article_type ~ ., data = training)
y_pred <- predict(classifier,testing[1:1997]) 
cm <- table(testing$article_type, y_pred) 

confusionMatrix(cm)
