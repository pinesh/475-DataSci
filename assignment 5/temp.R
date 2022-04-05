

#'   b. Classification (20%)
#'   For the final portion of this assignment, you will build and test a Naïve Bayes classifier
#'   with your data. First, you will need to use feature selection to reduce your feature set. A
#'   popular library for this is caret. It has many functionalities for reducing feature sets,
#'   including removing highly correlated features. You may wish to try several different
#'   methods to see which produces the best results for the following steps.
#'   Next, you will split your data into a training set and a test set. Your training set should
#'   comprise approximately 80% of your articles, however, you may try several sizes to find
#'   which produces the best results. Whatever way you split your training and test sets,
#'   however, you should try to ensure that your six article categories are equally represented
#'   in both sets.
#'   Next, you will build your Naïve Bayes classifier from your training data. The e1071
#'   package is most commonly used for this. Finally, you can use your model to predict the
#'   categories of your test data.
#'   Once you have produced a model that generates the best predictions you can get, print a
#'   confusion matrix of the results to demonstrate your completion of this task. For each
#'   class, give scores for precision (TruePositives / TruePositives+FalsePositives) and recall
#'   (TruePositives / TruePositives+FalseNegatives). To do this, you may want to use the
#'   confusionMatrix() function. 
#' #'
#' 
#' 
library("tidyverse")
library(dplyr)
# Loading package 
library(e1071) 
library(caTools) 
library(caret) 
article_type <- recode(originaldataset$section, 'culture'=0, 'sport'=1, 'technology'=2, 'world'=3,'artanddesign'=4,'business'=5,.default = 7)




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
#temp <- varImp(fit)
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

