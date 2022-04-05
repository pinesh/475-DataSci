library("tidyverse")
library(dplyr)

#read in precinct data
#precinct_house <- read.csv("2016-precinct-house.csv", header=TRUE) 

#precinct_house.texas <- filter(precinct_house, precinct_house$state_postal == "TX")
precinct_house.texas.dropped <- subset(precinct_house.texas,
                                       select = c(precinct,candidate_normalized,writein,party,votes))

#write.csv(precinct_house.texas.dropped,"PrecinctVoterData.csv")
precinct_house.texas.dropped$party <- str_replace(precinct_house.texas.dropped$party,fixed("republican"),"R")
precinct_house.texas.dropped$party <- str_replace(precinct_house.texas.dropped$party,fixed("democratic"),"D")
precinct_house.texas.dropped$party <- str_replace(precinct_house.texas.dropped$party,fixed("libertarian"),"I")
precinct_house.texas.dropped$party <- str_replace(precinct_house.texas.dropped$party,fixed("green"),"I")
precinct_house.texas.dropped$party[precinct_house.texas.dropped$candidate_normalized == "culler"] = "R"

precinct_1 <- subset(precinct_house.texas.dropped,votes != 0)
df <- aggregate(x = precinct_1$votes, by = list(precinct_1$precinct,precinct_1$party), FUN = sum)
colnames(df)<- c("precinct","party","votes")
write.csv(df,"PrecinctVoterData.csv")

precinct_dictrict_map<- read.csv("DistrictPrecinctIntersectionsR.csv", header=TRUE) 
precinct_dictrict_map <- subset(precinct_dictrict_map,
                                select = -c(X))
colnames(df)[colnames(df) == "precinct"] <- "PCTKEY"
district_votes = merge(x=df,y=precinct_dictrict_map,by="PCTKEY")
district_votes <- subset(district_votes,intesecting != 0)
district_votes <- subset(district_votes,
                         select = -c(PCTKEY))
district_votes$votes <- district_votes$votes*district_votes$intesecting
district_votes <- subset(district_votes,
                         select = -c(intesecting))
district_votes$votes<- as.integer(district_votes$votes+0.5)
district_votes <- subset(district_votes,votes != 0)
df_final <- aggregate(x = district_votes$votes, by = list(district_votes$party,district_votes$DISTRICT_N), FUN = sum)
colnames(df_final)<- c("PTY","DISTRICT_N","VOTES")
