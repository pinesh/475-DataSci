library("rjson")
library(tibble)
library(tidyr)
library(data.table)
library(reshape2)

raw <- (readLines("dev.jsonl"))
jsonr <- lapply(raw,fromJSON)

data_raw <- enframe(unlist(jsonr))

#create our new table, bind the names to the cols.
names <- c(unique(data_raw[["name"]]))
df <- data.frame()
for (k in names) df[[k]] <- as.character()

#this section is the slowest,done since data cols wasn't shared by all tables,
#potentially a better way to do this but this runs in O(n)
data_raw$marker = 0
count = 0

#assign a marker to each row so that they can be grouped out.
for(i in 1:nrow(data_raw)) {
  if(data_raw[i,1] == "phase") {
    count = count +1
  }
  
  data_raw[i,3 ] <- count
}

data_raw <-data_raw %>%
  group_by(marker)

df <- data.frame()

#lapply much faster, melt used to turn the long list to wide list format
news <- lapply(group_split(data_raw),
               function(x)reshape2::dcast(reshape2::melt(x, id.vars = c("name","value")), variable ~ name)) 

#result is bound to new table
df <- bind_rows(df,news)
df <- select (df,-c("variable"))
#retain order from json.
df<- df[,c(1,8,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17)]
write.csv(df,"wikisqlDevReformat.csv", row.names = FALSE)
