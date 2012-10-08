$(document).ready(function() {
    var refreshId = setInterval(function() {
        $('#live_play').load('/play/');
    }, 10000);

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

    $("#datepicker").datepicker({ dateFormat: "yyMdd", maxDate: "-1d", minDate: "2012Oct08" });
});

