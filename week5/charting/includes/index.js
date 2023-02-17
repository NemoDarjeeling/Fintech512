var ready = (callback) => {
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
  }
  
  ready(() => { 
      /* Do things after DOM has fully loaded */ 
      makeplot();
  });

function makeplot() {
    console.log("makeplot: start")
    fetch("includes/data/AAPL.csv")
    .then((response) => response.text()) /* asynchronous */
    .catch(error => {
        alert(error)
         })
    .then((text) => {
      console.log("csv: start")
      csv().fromString(text).then(processData)  /* asynchronous */
      console.log("csv: end")
    })
    console.log("makeplot: end")
  
};


function processData(data) {
  console.log("processData: start")
  let x = [], y = []

  for (let i=0; i<data.length; i++) {
      row = data[i];
      x.push( row['Date'] );
      y.push( row['Close'] );
  } 
  makePlotly( x, y );
  console.log("processData: end")
}

function makePlotly( x, y ){
  console.log("makePlotly: start")
  var traces = [{
        x: x,
        y: y
  }];
  var layout  = { title: "Apple Stock Price History"}

  myDiv = document.getElementById('myDiv');
  Plotly.newPlot( myDiv, traces, layout );
  console.log("makePlotly: end")
};

function submit() {
  bootbox.confirm({
    title: 'Submit?',
    message: 'Do you want to submit now?',
    buttons: {
      cancel: {
        label: 'Yes'
      },
      confirm: {
        label: 'No'
      }
    },
  });
}