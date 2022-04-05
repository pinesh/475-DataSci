library(rgdal)
library(rgeos)
library(sf,quietly=TRUE)
library(lwgeom)
library(sf)
library(tidyverse)
region_group <- subset(region_group,select =c(NEW,PTY))

district<-readOGR("./districts","School_Districts_1920")
district <- gBuffer(district, byid=TRUE, width=0)
sf_district <- st_as_sf(district)
sf_district <- merge(sf_district,region_join,by = "DISTRICT_N")

sf_temp <- sf_district %>% group_by(NEW) %>% summarise()

sf_temp  <- merge(sf_temp ,region_group,by = "NEW")

sf_temp$col <- "#FFFFFF" 
sf_temp$col[sf_temp$PTY == "R"] <- "#FF0000"
sf_temp$col[sf_temp$PTY == "C"] <- "#A901DB"
sf_temp$col[sf_temp$PTY == "D"] <- "#2E64FE"


ggplot(data = sf_temp) +
  ggplot2::geom_sf(fill = sf_temp$col)
ggsave("seats.png",width = 18, height = 18,dpi = 300,unit = "in")

nation<-readOGR("./PLANC235","PLANC235")
nation <- gBuffer(nation, byid=TRUE, width=0)
sf_nation <- st_as_sf(nation)
sf_nation$same <- 0
region_test <- gUnaryUnion(nation, id = nation$same)
sf_region_test <-st_as_sf(region_test)


old_map <- (st_perimeter(sf_region_test) -sum(st_perimeter(sf_nation))) /2
sf_temp_c <- as(sf_temp, 'Spatial')
sf_temp_c$same <-0
region_test_new <- st_as_sf(gUnaryUnion(sf_temp_c, id = sf_temp_c$same))

new_map <- (st_perimeter(region_test_new) -sum(st_perimeter(sf_temp))) /2
