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
      gridColor: "#A0A0A0"
      interlacedColor: "#d3d3d3"
    },
    axisY: {
      title: "People playing",
      titleFontSize: 24,
      prefix: ""
      gridColor: "#A0A0A0"
    },
    data: [{
      type: "stackedArea",
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

  $.getJSON("playing_r.json", addData);
}

function doreload(){
  document.getElementsByTagName("BODY")[0].style.display = "none";
  location.reload(true)
}
