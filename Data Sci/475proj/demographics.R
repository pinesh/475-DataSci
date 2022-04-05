school_demo<- read.csv("schoolpop.csv", header=TRUE) 
library(dplyr)
district_names =  subset(school_demo, select = c(ï..School.District) )[seq(1, nrow(school_demo), 2),]
school_demo = subset(school_demo, select = -c(ï..School.District,Black,Hisp,B.H,Other) )
  
school_demo %>%
  mutate_all(as.numeric)
sapply(school_demo, class) 

demo_nonblank <- school_demo[seq(1, nrow(school_demo), 2),]
demo_blank <- school_demo[seq(0, nrow(school_demo), 2),]
school_demo[seq(0, nrow(school_demo), 2), ] <- school_demo[seq(0, nrow(school_demo), 2), ] + school_demo[seq(1, nrow(school_demo), 2), ]
demo_sum <- school_demo[seq(0, nrow(school_demo), 2) ,]


library(tidyverse)
names_to_num <- subset(district@data,select = c(NAME,DISTRICT_N)) %>% 
  arrange((NAME))
testm <- crossing(names_to_num, demo_sum)
#demo_sum$NAME <- names_to_num$NAME
demo_sum$DISTRICT_N <-names_to_num$DISTRICT_N
demograph_mapped <- merge(demo_sum,unique(region_join),by = "DISTRICT_N")

regional_demographics <- aggregate(list(Total = demograph_mapped$Total,Anglo = demograph_mapped $Anglo), by=list(Region=demograph_mapped$NEW), FUN=sum)

x <- (regional_demographics$Total - regional_demographics$Anglo) / regional_demographics$Total
regional_demographics$percent_nonwhite = x
regional_demographics$majority <- 'W'
regional_demographics$majority[which(regional_demographics$percent_nonwhite > 0.50)] = 'M'

regional_demographics <- subset(regional_demographics,select = c(Region,majority,percent_nonwhite))
write.csv(regional_demographics,"RegionalDemographics.csv")