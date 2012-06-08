$(document).ready(function() {
    var refreshId = setInterval(function() {
        $('#live_play').load('/play/');
    }, 10000);
    
    $('a#feedbackbtn').mouseover(function() {
        $('#feedback').animate({'top': '0px'}, 400);
    });
    
    $('#info').mouseover(function() {
        $('#feedback').animate({'top': '-32px'}, 'slow');
    }); 
    
    $('a#tosopen').click(function() {
        $('#tos').show('slow');
    });

    $('a#tosexit').click(function() {
        $('#tos').hide('slow');
    });
    
    $('a#aboutopen').click(function() {
        $('#about').show('slow');
    });

    $('a#aboutexit').click(function() {
        $('#about').hide('slow');
    });
});
