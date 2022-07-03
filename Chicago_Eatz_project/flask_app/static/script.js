import fetch from "node-fetch"
// Initialize and add the map
async function initMap(latitude, longitude) {
    // The location of the restaurant
    const location = { lat: latitude, lng: longitude };
    // The map, centered at address 
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: location,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
        position: location,
        map: map,
    });
}

// does this need to be async?
async function get_map_data(){
    var response = await fetch("https://maps.googleapis.com/maps/api/geocode/json?address=233+N+Canal+Street,+Chicago,+IL&key=AIzaSyDZcxWYHmK8bi-Fzwnu2BDlLz5PTHEYjNs")
    var map_data = await response.json();
    var latitude = map_data.results[0].geometry.location.lat
    var longitude = map_data.results[0].geometry.location.lng;
    var coordinates = [latitude, longitude]
    return coordinates;
}
var address = "233 N Canal St Chicago, IL";
// how to get the address from my html document or from SQL?
var md = get_map_data();
console.log(md)


// window.initMap = initMap;