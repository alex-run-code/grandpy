

var map;
var service;
var infowindow;

document.getElementById('bijour').style = 'height: 20em; background: green';



function initMap() {
    var sydney = new google.maps.LatLng(-33.867, 151.195);
    infowindow = new google.maps.InfoWindow();

    newmap = document.createElement('div');
    document.getElementById('bijour').insertAdjacentElement('afterend', newmap);
    newmap.style = 'height: 20em'
    console.log('blowing a cock')

    map = new google.maps.Map(
        newmap, {center: sydney, zoom: 15});

    var request = {
        query: 'louvre',
        fields: ['formatted_address','name', 'geometry'],
    };

    service = new google.maps.places.PlacesService(map);

    service.findPlaceFromQuery(request, function(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            address = results[i].formatted_address
            latitude = results[i].geometry.location.lat()
            console.log(address)
            createMarker(results[i]);
        }

        map.setCenter(results[0].geometry.location);
        }
    });
}

function createMarker(place) {
var marker = new google.maps.Marker({
    map: map,
    position: place.geometry.location
});

google.maps.event.addListener(marker, 'click', function() {
    infowindow.setContent(place.name);
    infowindow.open(map, this);
});
}

var mybutton = document.getElementById('mybutton');
mybutton.addEventListener('click', function() {
    initMap();
    createMarker(place);
});
