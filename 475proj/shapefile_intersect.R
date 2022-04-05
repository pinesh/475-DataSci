library(rgdal)
library(rgeos)
library(sf,quietly=TRUE)

library(sf)
library(tidyverse)

precinct<-readOGR("./general/general","2016General")
district<-readOGR("./districts/districts","School_Districts_1920")

precinct <- gBuffer(precinct, byid=TRUE, width=0)
district <- gBuffer(district, byid=TRUE, width=0)



#----------------------------YES NO INTERSECTS---------------------------------
#Results <- st_intersection(st_as_sf(precinct),st_as_sf(district))
#intesecting_precincts  <- subset(Results,
                                # select = -c(COLOR,Shape_area,Shape_len,Shape_area.1,Shape_len.1,COLOR.1,DISTRICT,DISTRICT_C))

#intesecting_precincts  <- st_set_geometry(intesecting_precincts, NULL)

#write.csv(intesecting_precincts,"PrecinctToDistrict.csv")


#----------------------------% INTERSECTS---------------------------------
sf_precinct <- st_as_sf(precinct)
sf_district <- st_as_sf(district)

# intersect - note that sf is intelligent with attribute data!
pi <- st_intersection(sf_district,sf_precinct)

attArea <- pi %>% 
  mutate(area = st_area(.) %>% as.numeric())

precinct_areas  <- subset(sf_precinct,select = c(PCTKEY,Shape_area))
precinct_areas <- st_set_geometry(precinct_areas, NULL)

df = merge(x = attArea, y = precinct_areas, by = "PCTKEY")

df <- transform(df, intesecting = df$area / df$Shape_area.y )
results  <- subset(df,select = c(PCTKEY,DISTRICT_N,intesecting))
results <- st_set_geometry(results, NULL)

write.csv(results,"DistrictPrecinctIntersectionsR.csv")

#test whether the aggregation is all 1s (no % missing)
test <- aggregate(x = results$intesecting,                # Specify data column
                  by = list(results$PCTKEY),              # Specify group indicator
                  FUN = sum)                            # Specify function (i.e. sum)