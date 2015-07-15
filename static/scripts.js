$(document).ready(function () {
    $("#drop-zone").on("dragenter", function (event) {
        event.stopPropagation();
        event.preventDefault();
        $(this).addClass('drop');
    });

    $("#drop-zone").on("dragleave", function (event) {
        event.stopPropagation();
        event.preventDefault();
        $(this).removeClass('drop');
    });

    $("#drop-zone").on("dragover", function (event) {
        event.stopPropagation();
        event.preventDefault();
    });

    $(document).on('drop', function (event) {
        event.stopPropagation();
        event.preventDefault();
    });

    $("#drop-zone").on("drop", function (event) {
        event.stopPropagation();
        event.preventDefault();
        $(this).removeClass('drop');
        var files = event.originalEvent.dataTransfer.files;
        handleFileUpload(files.item(0));
    });

    $("#button-zone").change(function () {
        var files = $("#button-zone").prop('files');
        handleFileUpload(files.item(0));
    });

    function handleFileUpload(file) {
        var data = new FormData();        
        data.append('pic', file);
        data.append('size', $("#photo-size").val());
        $("#drop-zone").html('<span class="glyphicon glyphicon-refresh glyphicon-refresh-animate"></span>');
        $.ajax({
            url: '/upload',
            data: data,
            cache: false,
            contentType: false,
            processData: false,
            type: 'POST',
            success: function (data) {
                $("#drop-zone").text('Drag and drop another files here...');
                $("#ticket-image").attr("src", data);
            },
            error: function (data) {
                $("#drop-zone").html('Try with an image format file...');
            }
        });
    };   
});
