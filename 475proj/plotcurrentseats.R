precinct_house.texas <- filter(precinct_house, precinct_house$state_postal == "TX")
precinct_votes <- subset(precinct_house.texas,select = c(district,votes,party,candidate_normalized))
precinct_votes$party <- str_replace(precinct_votes$party,fixed("republican"),"R")
precinct_votes$party <- str_replace(precinct_votes$party,fixed("democratic"),"D")
precinct_votes$party <- str_replace(precinct_votes$party,fixed("libertarian"),"I")
precinct_votes$party <- str_replace(precinct_votes$party,fixed("green"),"I")
precinct_votes$party[precinct_votes$candidate_normalized == "culler"] = "R"
precinct_votes <- subset(precinct_votes,select = -c(candidate_normalized))

joinme <- precinct_8
joinme$district = 8
joinme <-subset(joinme,select = c(district,votes,party))

precinct_votes <-rbind(precinct_votes,joinme)

df_stn <- aggregate(x = precinct_votes$votes, by = list(precinct_votes$party,precinct_votes$district), FUN = sum)
colnames(df_stn)<- c("PTY","district","votes")

stn_totals = aggregate(x = precinct_votes$votes, by = list(precinct_votes$district), FUN = sum)
colnames(stn_totals)<- c("district","ttl_votes")

region_stn <- df_stn %>%   group_by(district) %>% 
  arrange(desc(votes)) %>% 
  slice(1) %>% 
  ungroup()


region_stn <- merge(region_stn,stn_totals)

x <- region_stn$votes/region_stn$ttl_votes
region_stn$percent = x


testm = subset(region_stn,select = c(percent,PTY))
testm$y = 1
testm$percent[which(testm$PTY == "D")] = 1-testm$percent[which(testm$PTY == "D")]

range<- colorRampPalette(c("blue", "red"))

x <-arrange(testm,testm$percent)
my_colors <- range(100) 

ats <- c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)

multip <- x$percent * 100 
multip <- as.integer(multip +0.5)
finalcol <- my_colors[multip]
x$col <-finalcol 
plabels <- c("100%","90%","80%","70%","60%","50%","60%","70%","80%","90%","100%")

library(ggplot2)


p2 <- ggplot(x, aes(percent, y)) +geom_point(shape = 19,colour=x$col,size=2)  +
  scale_x_discrete(expand = expand_scale(mult= c(0.221, 0.165)),"Percent Chance", labels = plabels, limits = ats) + scale_y_continuous(expand = c(0, 0),
                                                                                                                                    name = "Democratic Victory",sec.axis = sec_axis( trans=~.*1, name="Republican Victory")) +
  theme(axis.text.y = element_blank(),axis.ticks.y = element_blank()) + 
  labs(title = "Seat Probability", subtitle = "Percent chance a current district votes for a party")
ggsave("seatdistroSTDN.png",width = 20, height = 5,dpi = 300,unit = "in")



library(rgdal)
library(rgeos)
library(sf,quietly=TRUE)

library(sf)
library(tidyverse)

region_stn$PTY[which(region_stn$percent < 0.60)] = 'C'
region_stn <- subset(region_stn,select =c(district,PTY))
colnames(region_stn)<- c("District","PTY")

testc<-st_as_sf(nation)
sf_district_stn <- st_as_sf(nation)
sf_district_stn <- merge(sf_district_stn,region_stn,by = "District")

sf_temp_stn <- sf_district_stn %>% group_by(District) %>% summarise()

sf_temp_stn  <- merge(sf_temp_stn ,region_stn,by = "District")

sf_temp_stn$col <- "#FFFFFF"
sf_temp_stn$col[sf_temp_stn$PTY == "R"] <- "#FF0000"
sf_temp_stn$col[sf_temp_stn$PTY == "C"] <- "#A901DB"
sf_temp_stn$col[sf_temp_stn$PTY == "D"] <- "#2E64FE"


ggplot(data = sf_temp_stn) +
  ggplot2::geom_sf(fill = sf_temp_stn$col)
ggsave("seatsSTND.png",width = 18, height = 18,dpi = 300,unit = "in")


