// import fetch from "node-fetch"
// Initialize and add the map
async function initMap(latitude, longitude) {
    // The location of the restaurant
    const location = { lat: latitude, lng: longitude };
    // The map, centered at address 
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: location,
    });
    // The marker, positioned in the center
    const marker = new google.maps.Marker({
        position: location,
        map: map,
    });
}

// does this need to be async?
async function get_map_data(){
    var rest_address = document.getElementById("rest_address").value
    var response = await fetch("https://maps.googleapis.com/maps/api/geocode/json?address=" + rest_address + "&key=" + "AIzaSyDZcxWYHmK8bi-Fzwnu2BDlLz5PTHEYjNs")
    // var response = await fetch("https://maps.googleapis.com/maps/api/geocode/json?address=233+N+Canal+Street,+Chicago,+IL&key=AIzaSyDZcxWYHmK8bi-Fzwnu2BDlLz5PTHEYjNs")
    console.log(response)
    var map_data = await response.json();
    console.log(map_data)
    var latitude = map_data.results[0].geometry.location.lat
    var longitude = map_data.results[0].geometry.location.lng;
    // var coordinates = [latitude, longitude]
    // return coordinates;
    // var mainElement = document.querySelector("#map");
    // mainElement.innerHTML = map_data
    initMap(latitude, longitude)
}




// window.initMap = initMap;