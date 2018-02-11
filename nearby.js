


function getNearbyPlaces(latitude,longitude){
	var url = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location="
		+latitude+","+longitude+"&radius=5000&type=museum&key=AIzaSyDLSlQykTgmoe5ukRxrW6AAPA-42xp3hPA";
	$(document).ready(function(){
  			
		$.getJSON(url,function(data){
			console.log(data);
		});

	});
}

getNearbyPlaces(51.503186,-0.126446);