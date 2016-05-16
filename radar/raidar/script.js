var w = 350,
	h = 350;

var colorscale = d3.scale.category10();

//Legend titles
var LegendOptions = ["Year 2012", "Year 2013", "Year 2014", "Year 2015"];

d = [
  [
    {axis: "WTF", value: 5.768712},
    {axis: "news", value: 0.426729},
    {axis: "pcmasterrace", value: 0.000691},
    {axis: "nba", value: 1.080100},
    {axis: "AdviceAnimals", value: 3.280354},
    {axis: "videos", value: 3.200519},
    {axis: "worldnews", value: 2.007327},
    {axis: "todayilearned", value: 2.604053},
    {axis: "pics", value: 8.135308},
    {axis: "nfl", value: 2.102297},
    {axis: "funny", value: 10.867092},
    {axis: "leagueoflegends", value: 3.912651}
  ],
  [
    {axis: "WTF", value: 7.654763},
    {axis: "news", value: 1.652050},
    {axis: "pcmasterrace", value: 0.469178},
    {axis: "nba", value: 2.748301},
    {axis: "AdviceAnimals", value: 8.781397},
    {axis: "videos", value: 4.440903},
    {axis: "worldnews", value: 3.601042},
    {axis: "todayilearned", value: 4.247175},
    {axis: "pics", value: 9.154664},
    {axis: "nfl", value: 4.186025},
    {axis: "funny", value: 11.840901},
    {axis: "leagueoflegends", value: 7.264362}
  ],
  [
    {axis: "WTF", value: 5.265988},
    {axis: "news", value: 3.381131},
    {axis: "pcmasterrace", value: 3.368796},
    {axis: "nba", value: 4.710210},
    {axis: "AdviceAnimals", value: 8.508030},
    {axis: "videos", value: 5.478555},
    {axis: "worldnews", value: 5.380470},
    {axis: "todayilearned", value: 4.874763},
    {axis: "pics", value: 7.622404},
    {axis: "nfl", value: 5.576785},
    {axis: "funny", value: 10.149324},
    {axis: "leagueoflegends", value: 9.764849}
  ],
  [
    {axis: "WTF", value: 4.163445},
    {axis: "news", value: 5.894945},
    {axis: "pcmasterrace", value: 6.175437},
    {axis: "nba", value: 6.125096},
    {axis: "AdviceAnimals", value: 4.167775},
    {axis: "videos", value: 6.150983},
    {axis: "worldnews", value: 6.277836},
    {axis: "todayilearned", value: 5.832236},
    {axis: "pics", value: 7.080778},
    {axis: "nfl", value: 7.636164},
    {axis: "funny", value: 8.324695},
    {axis: "leagueoflegends", value: 11.560868}
  ]
];



//Options for the Radar chart, other than default
var mycfg = {
  w: w,
  h: h,
  maxValue: 2,
  levels: 10,
  ExtraWidthX: 200
}
var mycfg_cert = JSON.parse(JSON.stringify(mycfg)),
  mycfg_idse = JSON.parse(JSON.stringify(mycfg)),
  mycfg_stats = JSON.parse(JSON.stringify(mycfg)),
  mycfg_others = JSON.parse(JSON.stringify(mycfg));

mycfg_cert.color = d3.scale.ordinal().range(['#1F77B4']);
mycfg_idse.color = d3.scale.ordinal().range(['#FF7F0E']);
mycfg_stats.color = d3.scale.ordinal().range(['#2CA02C']);
mycfg_others.color = d3.scale.ordinal().range(['#D62728']);


//Call function to draw the Radar chart
//Will expect that data is in %'s
RadarChart.draw("#chart", d, mycfg);
// RadarChart.draw("#chart1", d_idse, mycfg_idse);
// RadarChart.draw("#chart2", d_stats, mycfg_stats);
// RadarChart.draw("#chart3", d_cert, mycfg_cert);
// RadarChart.draw("#chart4", d_others, mycfg_others);

////////////////////////////////////////////
/////////// Initiate legend ////////////////
////////////////////////////////////////////

var svg = d3.select('#combined')
	.selectAll('svg')
	.append('svg')
	.attr("width", w+300)
	.attr("height", h);

//Create the title for the legend
var text = svg.append("text")
	.attr("class", "title")
	.attr('transform', 'translate(90,0)') 
	.attr("x", w - 50)
	.attr("y", 10)
	.attr("font-size", "12px")
	.attr("fill", "#404040")
	.text("number of comments( * 1e6)	");
		
//Initiate Legend	
var legend = svg.append("g")
	.attr("class", "legend")
	.attr("height", 100)
	.attr("width", 200)
	.attr('transform', 'translate(90,20)') 
	;
	//Create colour squares
	legend.selectAll('rect')
	  .data(LegendOptions)
	  .enter()
	  .append("rect")
	  .attr("x", w - 45)
	  .attr("y", function(d, i){ return i * 20;})
	  .attr("width", 10)
	  .attr("height", 10)
	  .style("fill", function(d, i){ return colorscale(i);})
	  ;
	//Create text next to squares
	legend.selectAll('text')
	  .data(LegendOptions)
	  .enter()
	  .append("text")
	  .attr("x", w - 32)
	  .attr("y", function(d, i){ return i * 20 + 9;})
	  .attr("font-size", "11px")
	  .attr("fill", "#737373")
	  .text(function(d) { return d; })
	  ;	