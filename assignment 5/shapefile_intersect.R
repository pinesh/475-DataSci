library(rgdal)
library(rgeos)
precinct<-readOGR("./","Field")
district<-readOGR("./","Soil")
Results<-gIntersects(Soil,Field,byid=TRUE)


#rownames(Results)<-Field@data$FieldName
#colnames(Results)<-Soil@data$SoilType

