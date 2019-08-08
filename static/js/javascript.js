function ajaxPost(url, data, callback) {
    var req = new XMLHttpRequest ();
    req.open("POST", url);
    req.addEventListener('load', function() {
        if (req.status === 200) {
            callback(req.responseText)
        } else {
            console.error('Error')
        }
    });
    req.send(data);
}


var question = document.getElementById('question');
var sendQuestion = document.getElementById('sendQuestion');

// GOOGLE MAP // 

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

var map;
var service;
var infowindow;



function initMap(questionAsked) {
    var sydney = new google.maps.LatLng(-33.867, 151.195);
    infowindow = new google.maps.InfoWindow();

    newmap = document.createElement('div');
    newmap.style = 'height: 20em';
    infoLocation = {};

    map = new google.maps.Map(newmap, {center: sydney, zoom: 15});

    var request = {
        query: questionAsked,
        fields: ['formatted_address','name', 'geometry'],
    };

    service = new google.maps.places.PlacesService(map);

    service.findPlaceFromQuery(request, function(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            for (var i = 0; i < results.length; i++) {        
                infoLocation['streetAddress'] = results[i].formatted_address;
                infoLocation['latitude'] = results[i].geometry.location.lat();
                infoLocation['longitude'] = results[i].geometry.location.lng();
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


// FIN GOOGLE MAP //

sendQuestion.addEventListener('click', function (e) {

    var story =  ' Bien sûr mon petit ! Voici l\'adresse : ';
    document.getElementById('loading').style = 'display: block';
    
    e.preventDefault();

    var questionDisplayed = document.createElement('div');
    questionDisplayed.classList = 'col-md-8 speech-bubble sb-left hvr-pop';
    questionDisplayed.style = 'text-align: start; font-size: 1em';
    questionDisplayed.textContent = question.value;
    questionAsked = question.value;

    var sentQuestion = question.value;
    var sentQuestionToGoogle;

    ajaxPost('http://127.0.0.1:5000/api/', sentQuestion, function(reponse){
        sentQuestionToGoogle = reponse;
    });

    setTimeout(function() {


        console.log('SQTG : ' + sentQuestionToGoogle);

        initMap(sentQuestionToGoogle);

        var colmd4 = document.createElement('div');
        colmd4.className = 'col-md-4'; 

        var answerDisplayed = document.createElement('div');
        answerDisplayed.classList = 'col-md-8 offset-4 speech-bubble sb-right hvr-pop';
        answerDisplayed.style = 'text-align: justify; font-size: 1em;';

        var mapbubble = document.createElement('div');
        mapbubble.classList = 'col-md-8 offset-4 speech-bubble sb-right hvr-pop';
        mapbubble.style = 'height: 20em';
        newmap.style = 'height: 18em'
        mapbubble.insertAdjacentElement('afterbegin',newmap);

        setTimeout(function() {

            document.getElementById('loading').style = 'none';
            answerDisplayed.textContent = story + infoLocation['streetAddress'];
            document.getElementById('discussion').insertAdjacentElement('afterbegin', mapbubble);
            document.getElementById('discussion').insertAdjacentElement('afterbegin', answerDisplayed);
            document.getElementById('discussion').insertAdjacentElement('afterbegin', colmd4);
            document.getElementById('discussion').insertAdjacentElement('afterbegin', questionDisplayed);

        },1000);
    },1000);
});
