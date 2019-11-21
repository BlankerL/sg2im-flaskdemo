function submitForm() {
    $(document).ready(function () {
        var options = {
            target: '#result',   // target element(s) to be updated with server response
            url: '/api/parser',
            type: 'post',
            clearForm: false,
            resetForm: false
        };

        // bind to the form's submit event
        $('#form').ajaxSubmit(options);

        return false;
    });
}