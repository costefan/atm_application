$(document).ready(function () {
    $("input[type=text]").on('keydown', function(event) {
        event.preventDefault();
    });
    $("input[type=button]").on('click', function() {
        if ($("#money").val().length < 6) {
            if (this.value !== 'CLEAR') {
                $("#money").val($("#money").val() + this.value);
            }
            else {
                $("#money").val('');
            }
        }
    });
});