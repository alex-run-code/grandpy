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
var marker;

function initMap(latitude, longitude) {
    newmap = document.createElement('div');
    newmap.style = 'height: 20em';
    map = new google.maps.Map(newmap, {
        center: {lat: latitude, lng: longitude},
        zoom: 15,
    });

    marker = new google.maps.Marker({
        position: {lat: latitude, lng: longitude},
        map: map,
    });
}

sendQuestion.addEventListener('click', function (e) {

    e.preventDefault();
    document.getElementById('loading').style = 'display: block';
    
    var questionDisplayed = document.createElement('div');
    questionDisplayed.classList = 'col-md-8 speech-bubble sb-left hvr-pop';
    questionDisplayed.style = 'text-align: start; font-size: 1em';
    questionDisplayed.textContent = question.value;
    questionAsked = question.value;

    var colmd4 = document.createElement('div');
    colmd4.className = 'col-md-4';

    // var answerFromApi;
    // console.log('question asked : ' + questionAsked)
    var dictAnswer;

    ajaxPost('http://127.0.0.1:5000/api/', questionAsked, function(reponse){
        answerFromApi = reponse;
        dictAnswer = JSON.parse(answerFromApi);
    

    var grandpyIntro =  'Bien sûr mon petit ! Voici l\'adresse : ';

    //setTimeout(function() {

    document.getElementById('loading').style = 'none';
    initMap(dictAnswer['latitude'], dictAnswer['longitude']);

    var answerDisplayed = document.createElement('div');
    answerDisplayed.classList = 'col-md-8 offset-4 speech-bubble sb-right hvr-pop';
    answerDisplayed.style = 'text-align: justify; font-size: 1em;';

    var mapbubble = document.createElement('div');
    mapbubble.classList = 'col-md-8 offset-4 speech-bubble sb-right hvr-pop';
    mapbubble.style = 'height: 20em';
    newmap.style = 'height: 18em';
    mapbubble.insertAdjacentElement('afterbegin', newmap);

    var storyFromGrandpy = document.createElement('div');
    var pageLink = document.createElement('a');
    pageLink.href = dictAnswer['link'];
    pageLink.textContent = ' ' + '[En savoir plus]';
    storyFromGrandpy.classList = 'col-md-8 offset-4 speech-bubble sb-right hvr-pop';
    storyFromGrandpy.style = 'text-align: justify; font-size: 1em;';
    storyFromGrandpy.textContent = dictAnswer['story'];
    storyFromGrandpy.appendChild(pageLink);

    answerDisplayed.textContent = grandpyIntro + dictAnswer['address'];
    document.getElementById('discussion').insertAdjacentElement('afterbegin', storyFromGrandpy);
    document.getElementById('discussion').insertAdjacentElement('afterbegin', mapbubble);
    document.getElementById('discussion').insertAdjacentElement('afterbegin', answerDisplayed);
    document.getElementById('discussion').insertAdjacentElement('afterbegin', colmd4);
    document.getElementById('discussion').insertAdjacentElement('afterbegin', questionDisplayed);

    // },8000);
    });
}); 