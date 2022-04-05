#find the number of wasted votes for each set, 
#(take total sum of dem wasted = republican wasted / total)
library(tidyverse)

region_final[apply(region_final!=0, 1, all),]

write.csv(region_final,"regionvoting.csv")

region_fixed <-read.csv("regionvotingFIXED.csv", header=TRUE) 
region_effic.1 <- merge(region_effic,region_fixed, by = "NEW")
region_effic.1$wastedD = region_effic.1$DVOTE
region_effic.1$wastedD[which(region_effic.1$PTY == "D")] = region_effic.1$DVOTE[which(region_effic.1$PTY == "D")] - (region_effic.1$TTL_VOTES[which(region_effic.1$PTY == "D")]/2)
region_effic.1$wastedR = region_effic.1$RVOTE
region_effic.1$wastedR[which(region_effic.1$PTY == "R")] = region_effic.1$RVOTE[which(region_effic.1$PTY == "R")] - (region_effic.1$TTL_VOTES[which(region_effic.1$PTY == "R")]/2)
effic <- (sum(region_effic.1$wastedD)-sum(region_effic.1$wastedR))/sum(region_effic.1$TTL_VOTES)*100
wastedD <- sum(region_effic.1$wastedD)
wastedR <- sum(region_effic.1$wastedR)
