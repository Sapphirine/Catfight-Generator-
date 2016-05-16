

data=read.csv(file="d3_results.csv",head=TRUE,sep=",")
library(networkD3)
library(ggplot2)
library(igraph)
nodes=data[,c(1,2,3:158,159)]
links=data.frame(expand.grid(nodes$Observation,nodes$Observation))




link_weight=function(x){
  s=x['Var1']
  t=x['Var2']
  return (sum(nodes[s,][3:158]+nodes[t,][3:158]==2))}
wt=apply(links,1,link_weight)
links$wt=wt



nodes$id=nodes$Observation-1
nodes=nodes[c(160,2:159)]

links=links[links$Var1!=links$Var2,]
links$Var1=links$Var1-1
links$Var2=links$Var2-1

forceNetwork(Links = links[links$wt>=10,], Nodes = nodes, Source="Var1", Target="Var2",NodeID = "username", Group = "username",linkWidth = 1,linkColour = "#afafaf",charge=-50)




