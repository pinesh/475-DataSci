
testm = subset(region_effic,select = c(percent,PTY))
testm$y = 1
testm$percent[which(testm$PTY == "D")] = 1-testm$percent[which(testm$PTY == "D")]
#testm$percent[which(testm$PTY == "R")] = testm$percent[which(testm$PTY == "R")] -0.5 
#plot(testm$percent, testm$y, col=testm$percent)

range <- colorRampPalette(c("blue", "red"))   # Apply colorRampPalette

x <-arrange(testm,testm$percent)
my_colors <- range(100) 

ats <- c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)

multip <- x$percent * 100 
multip <- as.integer(multip +0.5)
finalcol <- my_colors[multip]
x$col <-finalcol 
plabels <- c("100%","90%","80%","70%","60%","50%","60%","70%","80%","90%","100%")


library(ggplot2)


p1 <- ggplot(x, aes(percent, y)) +geom_point(shape = 19,colour=x$col,size=1.7)  +
  scale_x_discrete(expand = expand_scale(mult= c(0.2, 0.14)),"Percent Chance", labels = plabels, limits = ats) + scale_y_continuous(expand = c(0, 0),
    name = "Democratic Victory",sec.axis = sec_axis( trans=~.*1, name="Republican Victory")) +
  theme(axis.text.y = element_blank(),axis.ticks.y = element_blank()) + 
   labs(title = "Seat Probability", subtitle = "Percent chance a fixed district votes for a party")
ggsave("seatdistro.png",width = 20, height = 5,dpi = 300,unit = "in")
                                                                                  
                                                                                       
p1