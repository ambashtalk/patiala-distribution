// function sendRequest() {
//   $.ajax({
//     data: {job: "search_area"},
//     type: "POST",
//     success: function callback(){
//       //ANY CODE IN SUCCESS
//       // alert("Data sent to python")
//     }});
// }

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(fillCordinates, showError);
  } else { 
   //
  }
}

function fillCordinates(position) {
  document.getElementById("latitude").setAttribute("value", position.coords.latitude);
  document.getElementById("longitude").setAttribute("value", position.coords.longitude);
}

function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      alert("User denied the request for Geolocation.");
      break;
    case error.POSITION_UNAVAILABLE:
      alert("Location information is unavailable.");
      break;
    case error.TIMEOUT:
      alert("The request to get user location timed out.");
      break;
    case error.UNKNOWN_ERROR:
      alert("An unknown error occurred.");
      break;
  }
}