$(document).ready(function () {
    $("input[type=password]").on('keydown', function(event) {
        event.preventDefault();
    });
    $("input[type=button]").on('click', function() {
        if (this.value === 'CLEAR') {
           $("#password").val('');
        }
        else if ($("#password").val().length < 4) {
            $("#password").val($("#password").val() + this.value);
        }
    });
});