<html>
<head>
	<script src="jquery-1.11.1.min.js"></script>
	<script src="jquery.canvasjs.min.js"></script>
	<script>
	window.onload = function() {
	 
	var dataPoints = [];
	 
	var chart = new CanvasJS.Chart("chartContainer", {
		animationEnabled: true,
		theme: "light2",
		zoomEnabled: true,
		title: {
			/*text: "Number of friends playing a steam game"*/
		},
		toolTip:{   
			content: "{y} playing at {x}"
		},
		axisX: {
			title: "Time",
			titleFontSize: 24,
			valueFormatString: "DDDD tt" ,
			prefix: "",
			interval: 0.5,
			intervalType: "day"
		},
		axisY: {
			title: "People playing",
			titleFontSize: 24,
			prefix: ""
		},
		data: [{
			type: "line",
			xValueFormatString: "hh:mm TT" ,
			dataPoints: dataPoints
		}]
	});

	function addData(data) {
		var dps = data.people_playing;
		for (var i = 0; i < dps.length; i++) {
			dataPoints.push({
				x: new Date(dps[i][0] * 1000),
				y: dps[i][1]
			});
		}
		chart.render();
	}
	 
	$.getJSON("data.json", addData);
	 
	}
	
	function doreload(){
		document.getElementsByTagName("BODY")[0].style.display = "none";
		location.reload(true)
	}
	var auto;
	function updateChart(auto) {
		$.getJSON("readdata.json", function(data) {
			dataPoints = []
			var dps = data.people_playing;
			for (var i = 0; i < dps.length; i++) {
				dataPoints.push({
					x: new Date(dps[i][0] * 1000),
					y: dps[i][1]
				});
			}
		}).error(function(event, jqxhr, exception) {
			alert("No graph data! (Try running start.bash)");
		});
		chart.render();
		if(auto == true){
			console.log("Automatic Refresh enabled");
			setTimeout(function(){updateChart(true)}, 1000);
		}
	}
	
	updateChart(true);
	</script>
</head>
<body>
	<h1>Chart:</h1>
	<div id="chartContainer" style="height: 370px; width: 100%; overflow:hidden;"></div>
	<!--<a onclick="updateChart()"><button>Get players now</button></a><a onclick="updateChart()"><button>Refresh graph</button></a>
	<div height="100%" width="100%" style="z-index: 10; display: none; background-color: white;" id="overlay"></div>-->
</body>
</html>