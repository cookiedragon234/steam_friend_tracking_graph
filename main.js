window.onload = function() {
  var dataPoints = [];
  var play = [];
  var online = [];

  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    theme: "light2",
    zoomEnabled: true,
    title: {
      /*text: "Number of friends playing a steam game"*/
    },
    /*toolTip:{
      content: "{y} at {x}"
    },*/
    axisX: {
      title: "Time",
      titleFontSize: 24,
      valueFormatString: "DDDD tt" ,
      prefix: "",
      interval: 0.5,
      intervalType: "day",
      gridColor: "#A0A0A0",
      interlacedColor: "#d3d3d3"
    },
    axisY: {
      title: "People playing",
      titleFontSize: 24,
      prefix: "",
      gridColor: "#A0A0A0"
    },
    data: [
      {
        type: "line",
        xValueFormatString: "hh:mm TT" ,
        dataPoints: play,
        legendText: "People playing",
        showInLegend: "true"
      },
      {
        type: "line",
        xValueFormatString: "hh:mm TT" ,
        dataPoints: online,
        legendText: "People online",
        showInLegend: "true"
      }
    ]
  });

  function addDataplay(data) {
    var dps = data.people_playing;
    for (var i = 0; i < dps.length; i++) {
      play.push({
        x: new Date(dps[i][0] * 1000),
        y: dps[i][1],
        toolTipContent: "{y} playing at {x}"
      });
    }
    renderit(play);
  }

  function addDataonline(data) {
    var dps = data.people_online;
    for (var i = 0; i < dps.length; i++) {
      online.push({
        x: new Date(dps[i][0] * 1000),
        y: dps[i][1],
        toolTipContent: "{y} online at {x}"
      });
    }
    $("#loading").hide();
    renderit(online);
    chart.render();
  }

  var ready = 0
  function renderit(which){
    if ready > 0{
      chart.render();
    } else{
      if which == "play"{
        ready = ready + 1;
      } else if which == "online"{
        ready = ready + 1;
      }
    }
  }

  $.getJSON("playing_r.json", addDataplay);
  $.getJSON("online_r.json", addDataonline);
}

function doreload(){
  document.getElementsByTagName("BODY")[0].style.display = "none";
  location.reload(true)
}
