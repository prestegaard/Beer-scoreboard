var socket;

function addBeerToServer(id, nickname) {
    if (confirm("Did " + nickname + " drink a new beer?") == true) {
        socket.emit('add beer', {data: id});
        //socket.emit('add beer', {data: 'I\'m connected!'});
    }
}

function doSomethingOnClick (){ alert( 'Clicked it!' ); }

$(document).ready(function(){
    //connect to the socket server.
    socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

    var number;
    var number_old;

    var nickname;
    var nickname_old;

    var last_seen;
    var last_seen_old;



    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    //receive details from server
    socket.on('nickname socket', function(msg) {
        nickname = msg.data;     
    });


    socket.on('beer socket', function(msg) {
        number = msg.data;
    });
    // Using third socket in the sequence to display received data
    socket.on('last seen socket', function(msg) {
        last_seen = msg.data;
        nickname_string = '';
        nickname_string = nickname_string + '<h1>' + 'Latest drinker: ' + nickname.toString() + '</h1>';

        number_of_beers_string = '';
        number_of_beers_string = number_of_beers_string + '<p><i>' + 'Number of beers: '  + number.toString() + '</i></p>';
        
        last_seen_string = '';
        last_seen_string = last_seen_string + '<p>' + 'Latest beer: ' + last_seen.toString() + '</p>';
        

        id_beer      = '#' + 'beer_' + nickname.toString();
        id_last_seen = '#' + 'last_' + nickname.toString();
        //if(nickname.toString == 'laowi')
        //id = '#' + 'Karlstad';
        $('#scoreboard_header').html(nickname_string);
        $(id_beer).html(number_of_beers_string);
        $(id_last_seen).html(last_seen_string);
    });

    socket.on('current leader socket', function(msg) {
        msg_string = msg.data;
        var array = msg_string.split(',');
        nickname = array[0];
        number_of_beers = array[1];
        var leader_string = '';
        leader_string = leader_string + '<h1>' + 'Current leader: ' + nickname.toString() + '[' + number_of_beers.toString() + ']' + '</h1>';
        $('#current_leader_header').html(leader_string);
    });


    socket.on('play sound socket', function(msg){
        var sound = msg.data;
        var sound_string = '';
        sound_string = '/static/sounds/sound' + sound.toString() + '.mp3';
        //var x = document.getElementById(sound_string);
        //x.play();
        var audio = new Audio(sound_string);
        audio.play();
    });

});