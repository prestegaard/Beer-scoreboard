
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    
    var number;
    var number_old;
    
    var nickname;
    var nickname_old;
    
    var last_seen;
    var last_seen_old;
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