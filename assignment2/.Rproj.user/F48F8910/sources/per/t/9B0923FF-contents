library("tidyverse")
library(ggplot2)
library(dplyr)
library(imager)

#-------------------------------------------------------PART 1
'
1. This exercise relates to the College data set, which can be found in the file College.csv on the
course’s public webpage (https://scads.eecs.wsu.edu/index.php/datasets/). The dataset contains a
number of variables for 777 different universities and colleges in the US. The variables are
'


#'(a) Use the read.csv() function to read the data into R, or the csv library to read in the
#'data with python. In R you will load the data into a dataframe. In python you may store it as a list
#'of lists or use the pandas dataframe to store your data. Call the loaded data college. Ensure that
#'your column headers are not treated as a row of data. 

college<-read.csv("college.csv", header=TRUE)


#'(b) Find the median cost of books for all schools in this dataset.'

summary(college)
#median cost of books = 500


#'(c) Produce a scatterplot that shows a relationship between two numeric (not factor or boolean) 
#'features of your choice in the dataset. Ensure it has appropriate axis labels and a title. '

plot(college$Personal,college$Room.Board,xlab='Personal Spending',
     ylab='Room and Board costs',main='Personal Budgeting vs Room and Board')


#'(d) Produce a histogram showing the overall enrollment numbers (P.Undergrad plus
#'F.Undergrad) for both public and private (Private) schools. You may choose to show both on a
#'single plot (using side by side bars) or produce one plot for public schools and one for private
#'schools. Ensure whatever figures you produce have appropriate axis labels and a title. '

private <- subset(college,Private == "Yes")
public <- subset(college,Private == "No")


#-------------------------------------------------------PRIVATE
private_data <- data.frame(
  type = c("private full time" ,"private part time"  ),
  value = c( private$F.Undergrad,private$P.Undergrad )
)

private_plot <- private_data %>%
  ggplot( aes(x=value, fill=type)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity',binwidth = 100) +
  scale_fill_manual(values = c("#96b3a2","#404080" )) +
  labs(fill="",title = "Distribution of full and part time undergrads in private schools.",
  x = "Student Population" , y = "Frequency")


#-------------------------------------------------------PUBLIC
public_data <- data.frame(
  type = c("public full time" ,"public part time"  ),
  value = c( public$F.Undergrad,public$P.Undergrad )
)

public_plot <- public_data %>%
  ggplot( aes(x=value, fill=type)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity',binwidth = 100) +
  scale_fill_manual(values = c("#96b3a2","#404080" )) +
  labs(fill="",title = "Distribution of full and part time undergrads in public schools.",
       x = "Student Population" , y = "Frequency")


#-------------------------------------------------------PRINT PLOTS
png(filename="private.png",width=1000, height=1000)
print(private_plot)
dev.off()


im<-load.image("private.png")
plot(im)

png(filename="public.png",width=1000, height=1000)
print(public_plot)
dev.off()


im<-load.image("public.png")
plot(im)

#'(e) Create a new qualitative variable, called Top, by binning the Top10perc variable into
#'two categories (Yes and No). Specifically, divide the schools into two groups based on whether
#'or not the proportion of students coming from the top 10% of their high school classes exceeds
#'75%.'

college <- transform(college, Top = ifelse(Top10perc >= 75, "Yes", "No"))
college <- transform(college, Accept.Rate = Accept / Apps)

top_schools <- college$Accept.Rate[which(college$Top=="Yes")]
not_schools <- college$Accept.Rate[which(college$Top=="No")]


#'Now produce side-by-side boxplots of the schools' acceptance rates (based on Accept and Apps)
#'for each of the two Top categories. There should be two boxes on your figure, one for top
#'schools and one for others. How many top universities are there?
  
boxplot(top_schools,not_schools, main = "Acceptance rates of top schools vs other", 
        ylab = "Acceptance Rate", names = c("Top 10% Schools", "Other"))



top_colleges <- college[college$Top == "Yes", ] 

nrow(top_colleges) #NROW = 26, Therefore there are 26 top universities


#'(f) Continue exploring the data, producing two new plots of any type, and provide a brief
#'(one to two sentence) summary of your hypotheses and what you discover. Feel free to think
#'outside the box on this one but if you want something to point you in the right direction, look at
#'the summary statistics for various features, and think about what they tell you. Perhaps try
#'plotting various features from the dataset against each other and see if any patterns emerge. ''


#-------------------------------------------------------compare room and board with public and private 
private_room <- private$Room.Board
public_room <- public$Room.Board

boxplot(private_room,public_room, main = "Room and board, public vs private", 
        ylab = "Room and board price", names = c("private", "public"))

#In most to all cases, on average, Room and Board expenses are greater for private universities 
#than they are for their public counterparts.


#-------------------------------------------------------compare expenditures with out of state tuition cost
expenses = college$Expend  
tuition = college$Outstate
plot(expenses, tuition,main = "tution costs vs the amount spent on students",
     xlab="Instructional expenditure", ylab="tution costs")

#Tuition costs appear to rise at a rate much faster than the expenditure per student increases. 



#-------------------------------------------------------PART 2


#'2. This exercise involves the Auto.csv data set found on the course website. The features of the
#'dataset are as follows:
#'  • mpg: miles per gallon
#'  • cylinders: number of cylinders
#'  • displacement: volume of air displaced by cylinders
#'  • horsepower: power of the car (rate of work)
#'  • weight: how much the car weighs in lb
#'  • acceleration: rate at which car accelerates
#'  • year: when the car was made
#'  • origin: where the car comes from (1=USA, 2=Germany, 3=Japan)
#'  • name: the make and model of the car
#'  Make sure that rows with missing values have been removed from the data. For part, show both
#'  the code you used and any relevant outputs.

#'  (a) Specify which of the predictors are quantitative (measuring numeric properties such
#'  as size, or quantity), and which are qualitative (measuring non-numeric properties such as color,
#'  appearance, type etc.)? Keep in mind that a qualitative variable may be represented as quantitative type in the dataset,
#'   or the reverse. You may wish to adjust the types of your variables based on your findings.


#'Quantitative predictors:
# 'o	MPG
# 'o	Cylinders
# 'o	Displacement
# 'o	Horsepower
# 'o	Weight
# 'o	Acceleration
# 'o	Year
#'
#'Qualitative predictors:
# 'o	Name
# 'o	Origin



#'  (b) What is the range, mean and standard deviation of each quantitative predictor?
#'  
#read in data
autos<-na.omit(read.csv("auto.csv", header=TRUE))
autos$horsepower <- as.numeric(as.character(autos$horsepower))

#remove missing rows
autos <- autos[complete.cases(autos),]

summary(autos)

#-------------------------------------range and Sd for B
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


#-------------------------------------RESULTS B
#'Quantitative predictors:
#'•	MPG
#'•	Range:37.6
#'•	Mean: 23.45
#'•	Std: 7.805007
#'
#'•	Cylinders
#'•	Range:5
#'•	Mean:5.472
#'•	Std: 1.705783
#'
#'•	Displacement
#'•	Range:387
#'•	Mean:194.4
#'•	Std: 104.644
#'
#'•	Horsepower
#'•	Range:184
#'•	Mean:104.5
#'•	Std: 38.49116
#'
#'•	Weight
#'•	Range: 3527
#'•	Mean:2978
#'•	Std: 849.4026
#'
#'•	Acceleration
#'•	Range: 16.8
#'•	Mean:15.54
#'•	Std: 2.758864
#'
#'o	Year
#'•	Range:12
#'•	Mean: 75.98
#'•	Std: 3.683737



#'  (c) Now remove the 40th through 80th (inclusive) observations from the dataset. What is
#'  the range, mean, and standard deviation of each predictor in the subset of the data that remains?

#remove 40->80 inclusive
autosC <- autos[-c(39:79),] 

#get the mean
summary(autosC)

#-------------------------------------range and Sd
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

#-------------------------------------RESULTS C
#'Quantitative predictors:
#'o	MPG
#'•	Range: 37.6
#'•	Mean: 23.95
#'•	Std: 7.809443
#'
#'o	Cylinders
#'•	Range:5
#'•	Mean:5.413
#'•	Std: 1.663988
#'
#'o	Displacement
#'•	Range: 387
#'•	Mean:190.2
#'•	Std: 101.1749
#'
#'o	Horsepower
#'•	Range: 184
#'•	Mean:102.8
#'•	Std: 37.52519
#'
#'o	Weight
#'•	Range: 3348
#'•	Mean:2943
#'•	Std: 812.3924
#'
#'o	Acceleration
#'•	Range: 16.8
#'•	Mean:15.59
#'•	Std: 2.722163
#'
#'•	Year
#'•	Range:12
#'•	Mean: 76.5
#'•	Std: 3.546323
#'
#'  (d) Using the full data set, investigate the predictors graphically, using scatterplots,
#'  correlation scores or other tools of your choice. Create a correlation matrix for the relevant
#'  variables.

#install.packages("psych")


library(psych)

autos_numeric <- subset(autos, select=-c(name,origin))

pairs.panels(autos_numeric, method = "pearson", density = TRUE, 
             ellipses = TRUE,main = "Significance correlation of auto predictors")


#'  (e) Suppose that we wish to predict gas mileage (mpg) on the basis of the other variables.
#'  Which, if any, of the other variables might be useful in predicting mpg? Justify your answer
#'  based on the prior correlations.
#'  
#'Based on the correlation matrix,  The most likely candidates for predicting mileage would be 
#'cylinders displacement and horsepower , being that they all strongly correlate negatively with mileage,
#' The hypothesis would be whether cars with larger engines and power typically have worse mileage compared to 
#' smaller low powered engines. 


