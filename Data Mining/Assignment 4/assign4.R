
#'Problem 1(50 pts)

#install.packages("nycflights13")
library(nycflights13) 
library("tidyverse")
library(maps)
library(dplyr)
library(ggplot2)

#data(package = "nycflights13")
flights=as.data.frame(flights)
weather = as.data.frame(weather)
airports = as.data.frame(airports)


#'a.(10/9 pts)
flights_a <-(filter(flights, dest == 'TPA'))
flights_a<- filter(flights_a, time_hour >= '2013-11-01 12:00:00' & 
                     time_hour <= '2013-11-01 24:00:00')
flights_a <- subset(flights_a,select = 
                      c("tailnum","year","month","day","hour","origin"))
weather_a <-subset(weather,select = 
                     c("year","month","day","hour","origin","humid"))
answer_a <- left_join(flights_a, weather_a, by = 
                        c("year","month","day","hour","origin"), suffix = 
                        c("_flights", "_weather"))
head(answer_a)


#'b.(10/9 pts) 

#an anti join will return all rows from x where there are not matching values 
#in y, keeping only the columns from x,thus, the first will return all rows from
#flights that have no matching values in airports, while the second returns all
#rows from airports that have no matching values in flights.

#'c.(10/9 pts) 

answer_c <- inner_join(x=flights,y=airports,by = c("origin" = "faa"),
                       all.x=FALSE, all.y=FALSE)
answer_c <- inner_join(x=answer_c,y=airports,by = c("dest" = "faa"),
                       all.x=FALSE, all.y=FALSE)
answer_c <-subset(answer_c,select = c("name.x",
                                      "lat.x","lon.x","name.y","lat.y","lon.y"))
head(answer_c)


#'d.(10/9 pts) 

testflights <- na.omit(flights)
answer_d <- testflights %>% group_by(origin,dest) %>% 
  summarise(count = n_distinct(c(origin,dest)))
nrow(answer_d)
#I'm unsure of how we ended up with the extra unique combos but we did, 


#'e.(10/9 pts) 

answer_e <- testflights %>%
  group_by(origin,dest) %>%
  summarise_at(vars(air_time),
               list(avg_air = mean))

airports_e <- airports%>% right_join(answer_e,c("faa"="dest"))
airports_e <- na.omit(airports_e)

p <-ggplot(airports_e,aes(lon,lat))+
  borders("state")+
  geom_point(aes(colour = avg_air))+
  coord_quickmap()+
  labs(title = "Average destination travel times", 
       subtitle = "Plot of destination air times",
       caption = "Data source: nycflights13")
print(p)

#'
#'Problem 2 (30 pts)
#'  

#?register_google
library(ggmap)

warmupdat <- read.csv("warmupcsv.csv",header = FALSE,quote = "\"" )
addrs <- warmupdat[1]
#geocodes <- geocode(as.character(warmupdat$addr))
#warmupdat <- data.frame(warmupdat[,1:2],geocodes)


#this would've been how I got the lat and long for my data, however, geocoding 
#would've required signing up to either Google or Bings api which required
#credit card info and convoluted trials/billing plans. 

#instead I used geocode.localfocus.nl and pasted the unique contents of my 
#csv instead. 
#and will load the resulting csv.

warmupdat_complete <- distinct(read.csv("warmuplatlon.csv",
                                        header = FALSE,quote = "\""))
warmupdat<- left_join(addrs, warmupdat_complete, by = c("V1" = "V1"))

warm_group <- warmupdat %>%
  group_by(V1) %>%
  summarize(count = n())

warmupdat_complete <- left_join(warmupdat_complete, 
                                warm_group, by = c("V1" = "V1"))
warmupdat_complete$count=as.numeric(warmupdat_complete$count) 
colnames(warmupdat_complete) <- c("location", "latitude", "longitude","count") 
q <-ggplot(warmupdat_complete,aes(longitude,latitude))+
  borders("world")+
  theme_classic() +
  geom_point(aes(size = count),color = "blue")+
  coord_quickmap()+
  labs(title = "Origin of 475/575 students", 
       subtitle = "size corresponding to count",
       caption = "Data source: warmup.txt")
print(q)

#'
#'Problem 3 (20 pts)
#'  


#for this problem I followed an excellent tutorial online, I chose to use 
#the entire bee movie script as my example text.
library("tm")
library("wordcloud")
library("RColorBrewer")

text <- readLines("beemovie.txt")

# Load the data
docs <- Corpus(VectorSource(text))

# Convert the text to lower case, removing whitespace, stopwords, punctuation and
#setting it all to lowercase
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)

dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)

#"WordCloud of the entire Bee Movie script"
wordcloud(words = d$word, freq = d$freq, min.freq = 8,
          max.words=250, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(12, "Paired"))