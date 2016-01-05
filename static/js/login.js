$(document).ready(function () {
    maskCode();
    $("input[type=text]").on('keydown', function(event) {
        event.preventDefault();
    });
    $("input[type=button]").on('click', function() {
        if (this.value !== 'CLEAR') {
            $("#id_number").val($("#id_number").val() + this.value);
            maskCode();
        }
        else {
            $("#id_number").val('');
        }
    });
});


function maskCode() {
    $("#id_number").mask("?9999-9999-9999-9999");
}