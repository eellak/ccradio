$(document).ready(function() {
    var refreshId = setInterval(function() {
        $('#live_play').load('/play/');
    }, 100000);
    
    $('a#tosopen').click(function() {
        $('#tos').show('slow');
    });

    $('a#tosexit').click(function() {
        $('#tos').hide('slow');
    });
});
