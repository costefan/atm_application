$(document).ready(function () {
    $("input[type=password]").on('keydown', function(event) {
        event.preventDefault();
    });
    $("input[type=button]").on('click', function() {
        if ($("#password").val().length < 4) {
            if (this.value !== 'CLEAR') {
                $("#password").val($("#password").val() + this.value);
            }
            else {
                $("#password").val('');
            }
        }
    });
});