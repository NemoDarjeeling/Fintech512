var ready = (callback) => {
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
  }
  
  ready(() => { 
      makeplot();
  });

function makeplot() {
  document.getElementById("stock-select").addEventListener("change", function(){
    fetch("includes/data/" + this.value + ".csv")
    .then((response) => response.text())
    .catch(error => {
        alert(error)
    })
    .then((text) => {
      csv().fromString(text).then((data) => {
        processData(data, this.value)
      })
    })
  });  
};


function processData(data, stock) {
  console.log("processData: start")
  let x = [], y = []

  for (let i=0; i<data.length; i++) {
      row = data[i];
      x.push( row['Date'] );
      y.push( row['Close'] );
  } 
  makePlotly( x, y, stock );
  console.log("processData: end")
}

function makePlotly( x, y, stock ){
  console.log("makePlotly: start")
  var traces = [{
        x: x,
        y: y
  }];
  var layout  = { title: stock}

  myDiv = document.getElementById('myDiv');
  Plotly.newPlot( myDiv, traces, layout );
  console.log("makePlotly: end")
};

var dropdown = document.getElementById("stock-select");
dropdown.addEventListener("change", function() {
    var selectedValue = dropdown.value;
    var url = `includes/data/${selectedValue}.csv`;
    fetch(url).then((response) => response.text()).then((text) => {
        csv().fromString(text).then(processData);
    })
    .catch(error => {
        alert(error);
    });
});

function submit() {
  bootbox.confirm({
    title: "Submit?",
    message: "Are you sure you want to submit now?",
    buttons: {
      cancel: {
        label: '<i class="fa fa-times"></i> No'
      },
      confirm: {
        label: '<i class="fa fa-check"></i> Yes'
      }
    },
    callback: function(result) {
      if (result) {
        let dialog = bootbox.dialog({
          title: 'Submitting Form',
          message: '<p><i class="fas fa-spin fa-spinner"></i> Loading...</p>'
        });
        dialog.init(function() {
          setTimeout(function() {
              dialog.find('.bootbox-body').html('Form Submitted!');
          }, 900);
        });
      }
      else {
        let dialog = bootbox.dialog({
          title: 'Cancelling Action',
          message: '<p><i class="fas fa-spin fa-spinner"></i> Loading...</p>'
        });
        dialog.init(function() {
          setTimeout(function() {
              dialog.find('.bootbox-body').html('Action Cancelled!');
          }, 900);
        });
      }
    }
  });
}





