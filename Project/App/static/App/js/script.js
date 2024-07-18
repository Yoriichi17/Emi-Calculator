$(document).ready(function() {
    $('#emiForm').on('submit', function(event) {
        event.preventDefault();

        var principal = parseFloat($('#principal').val());
        var rate = parseFloat($('#rate').val());
        var time = parseFloat($('#time').val());

        $.ajax({
            url: '/calculate_emi/',
            type: 'POST',
            data: {
                'principal': principal,
                'rate': rate,
                'time': time,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                $('#result').html('Your EMI is: ' + response.emi);
            }
        });
    });
});
