$(document).ready(function () {
    eel.expose(DisplayText)
    function DisplayText(text) {
        $('.siri-message li:first').text(text);
        $('.siri-message').textillate('start');
    }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $('#Oval').attr('hidden', false);
        $('#siri-message').attr('hidden', true);
    }

});

