#regionmap <- read.csv("regions.csv", header=TRUE)
regionmap <- read.csv("big_full2.csv", header=TRUE)
newregion <- read.csv("centroid_manually_reshaped.csv", header=TRUE) 

regionmap[is.na(regionmap)] <- 0

regionmap = merge(x=regionmap,y=newregion,by="DISTRICT_N",all=TRUE)
#which(is.na(regionmap$NEW))
regionmap$NEW[which(is.na(regionmap$NEW))] = regionmap$REGION[which(is.na(regionmap$NEW))]
regionmap2 <- subset(regionmap,
                         select = c(PTY,VOTES,NEW))

region_final <- aggregate(x = regionmap$VOTES, by = list(regionmap$PTY,regionmap$NEW), FUN = sum)
region_final <- na.omit(region_final)
colnames(region_final)<- c("PTY","NEW","VOTES")

region_group <- region_final %>%   group_by(NEW) %>% 
  arrange(desc(VOTES)) %>% 
  slice(1) %>% 
  ungroup()



test <- aggregate(regionmap2$VOTES, by=list(Category=regionmap2$NEW), FUN=sum)

colnames(test)<- c("NEW","TTL_VOTES")
region_group = merge(x=region_group,y=test,by="NEW",all=TRUE)

x <- region_group$VOTES/ region_group$TTL_VOTES
region_group$percent = x
region_effic <- region_group
region_group$PTY[which(region_group$percent < 0.60)] = 'C'

regionmap <- subset(regionmap,
                    select = -c(PTY))
regionmap = merge(x=regionmap,y=region_group,by="NEW",all=TRUE)
regionmap <- subset(regionmap,
                    select = -c(REGION))
regionmap <- na.omit(regionmap) 
region_join <-subset(regionmap,select = c(DISTRICT_N,NEW,PTY))

write.csv(region_group,"electoraloutcome.csv")
