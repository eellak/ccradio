$(document).ready(function() {
    var refreshId = setInterval(function() {
        $('#live_play').load('/play/');
    }, 100000);
});
