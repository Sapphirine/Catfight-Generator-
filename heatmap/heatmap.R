##############################
# Heatmap Plotting
##############################
library(gplots)
library(RColorBrewer)

skills <- read.csv("season2015log.csv", header=TRUE, sep=",")

# Check out the column names
names(skills)

# Rename the rows, then remove the first column that used to contain the names
row.names(skills) <- skills[,1]
skills <- skills[,-1]

# Rename the columns, then re-order (though reordering isn't useful for heatmap.2 due to clustering)
names(skills) <- c('1st quarter', '2nd quarter', '3rd quarter', '4th quarter')

# Color Brewer color scale
color_scale = colorRampPalette(brewer.pal(9, 'YlOrRd'))(100)

# Convert to data matrix for heatmap use
skills_matrix <- data.matrix(skills)

# Heatmap without scale

jpeg(file="filename.jpg",quality = 1000,pointsize = 35,height=2160,width=1800)
heatmap.2(skills_matrix, Colv ="null", Rowv = "nill", dendrogram="none", scale="none", trace="none", col=color_scale, 
                          margins=c(6,10), cexCol=1, cexRow=1, srtCol=50, key=TRUE, keysize=1.5,
                          xlab="Quarters", ylab="Subreddit", sepwidth=c(0.01, 0.01), sepcolor="white")
dev.off()



# Large scale for export
skills_heatmap <- heatmap.2(skills_matrix, dendrogram="none", scale="none", trace="none", col=color_scale, 
                            margins=c(10,13), cexCol=1, cexRow=1, srtCol=45, key=TRUE, keysize=1.5,
                            xlab="Program", ylab="Technology", lwid=c(0.5, 0.5))

# With dendrogram
jpeg(file="filename.jpg",quality = 100,pointsize = 30,height=1800,width=1540)
heatmap.2(skills_matrix, dendrogram="none", Colv ="null", scale="none", trace="none", col=color_scale, 
                            margins=c(6,10), cexCol=1, cexRow=1, srtCol=50,
                            xlab="Quarters", ylab="Subreddit", sepwidth=c(0.01, 0.01), sepcolor="white")
dev.off()

