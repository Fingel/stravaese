//Globals
var rideMap

//Load ride path from the strava api and display it on a map.
function loadRidePath(rideId, map){
	url = "/ride/" + rideId + "/path"
	$.getJSON(url, function(data){
		if(rideMap){
			rideMap.setMap(null)
		}
		var ridePath = []
		bounds =  new google.maps.LatLngBounds()
		$(data.latlng).each(function(index){
			p = new google.maps.LatLng(data.latlng[index][0], data.latlng[index][1])
			ridePath.push(p)
			bounds.extend(p)
		})
		rideMap = new google.maps.Polyline({
			path: ridePath,
			strokeColor: "#FF0000",
	    		strokeOpacity: 1.0,
	    		strokeWeight: 2
 		});
 		rideMap.setMap(map);
 		map.fitBounds(bounds)
	});
}

function isNumeric(n) {
	return !isNaN(parseFloat(n)) && isFinite(n);
}
