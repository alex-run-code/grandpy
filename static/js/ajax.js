console.log('ca marche');


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
var story = `
Les Belles Histoires du père Castor est une série d’animation de 1993. 
Histoires qui commencent toujours une introduction du père castor qui sera ensuite le narrateur, 
facilitant la compréhension de ce qui est vu en même temps. Les dessins sont inégaux.
`
sendQuestion.addEventListener('click', function (e) {
    var comList = [];
    e.preventDefault();
    var questionDisplayed = "<div class='col-md-8 speech-bubble sb-left hvr-pop' style='text-align: start; font-size: 1em'>" + question.value + "</div><div class='col-md-4'></div>";
    var answerDisplayed = "<div class='col-md-8 offset-4 speech-bubble sb-right hvr-pop' style='text-align: justify; font-size: 1em;'>" + story + " </div>";
    comList.push(questionDisplayed, answerDisplayed);

    for (i=0; i < comList.length ; i++) {
        document.getElementById('discussion').insertAdjacentHTML('beforeEnd', comList[i]);
    }
    
    // sentQuestion = question.value;
    // ajaxPost('urldenotreserveurweb', sentQuestion)
    // initMap() - pour actualiser la map de google map

    question.value = '';
});

console.log('ca marche');