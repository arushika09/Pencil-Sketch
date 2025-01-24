$(document).ready(function() {
    $('#upload-form').submit(function(event) {
        event.preventDefault();

        var formData = new FormData($(this)[0]);

        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                if (response.error) {
                    console.error('Error:', response.error);
                } else {
                    $('#pencil-sketch-img').attr('src', 'data:image/jpeg;base64,' + response.pencil_sketch);
                }
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});
