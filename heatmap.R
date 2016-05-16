##############################
# Heatmap Plotting
##############################
library(gplots)
library(RColorBrewer)

skills <- read.csv("skills.csv", header=TRUE, sep=",")

# Check out the column names
names(skills)

# Rename the rows, then remove the first column that used to contain the names
row.names(skills) <- skills[,1]
skills <- skills[,-1]

# Rename the columns, then re-order (though reordering isn't useful for heatmap.2 due to clustering)
names(skills) <- c('Data Science Certification', 'MS, Data Science', 'MA, Statistics', 'Others')
skills <- skills[, c(2,1,3,4)]

# Color Brewer color scale
color_scale = brewer.pal(9, 'YlOrRd')

# Convert to data matrix for heatmap use
skills_matrix <- data.matrix(skills)

# Heatmap without scale
skills_heatmap <- heatmap.2(skills_matrix, dendrogram="none", scale="none", trace="none", col=color_scale, 
                          margins=c(10,13), cexCol=1, cexRow=1, srtCol=50, key=FALSE, keysize=0,
                          xlab="Program", ylab="Technology", sepwidth=c(0.15, 0.15), sepcolor="white")

# Large scale for export
skills_heatmap <- heatmap.2(skills_matrix, dendrogram="none", scale="none", trace="none", col=color_scale, 
                            margins=c(10,13), cexCol=1, cexRow=1, srtCol=45, key=TRUE, keysize=1.5,
                            xlab="Program", ylab="Technology", lwid=c(0.5, 0.5))

# With dendrogram
skills_heatmap <- heatmap.2(skills_matrix, scale="none", trace="none", col=color_scale, 
                            margins=c(10,13), cexCol=1, cexRow=1, srtCol=50,
                            xlab="Program", ylab="Technology", sepwidth=c(0.15, 0.15), sepcolor="white")