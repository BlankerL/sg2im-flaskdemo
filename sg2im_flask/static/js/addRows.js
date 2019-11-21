function addRow(){
    $("#table").each(
        function () {
            let rowId = Number($('#table tr:last td label').text());

            let tds = '<tr>';
            tds += '<td>' + '<label id="Document ID">' + (rowId + 1) + '</label>' + '</td>';
            tds += '<td>' + '<input type="text" name="obj1-' + (rowId + 1) +'"/>' + '</td>';
            tds += '<td>' + '<select name="rel-' + (rowId + 1) + '">'
                + '<option value="on">on</option>' +
                '<option value="in">in</option>' +
                '<option value="by">by</option>' +
                '<option value="above">above</option>' +
                '<option value="below">below</option>' +
                '<option value="behind">behind</option>' +
                '<option value="next to">next to</option>' +
                '<option value="standing on">standing on</option>' +
                '<option value="in front of">in front of</option>'
                + '</select>' + '</td>';
            tds += '<td>' + '<input type="text" name="obj2-' + (rowId + 1) +'"/>' + '</td>';
            tds += '</tr>';

            if ($('tbody', this).length > 0) {
                $('tbody', this).append(tds);
            } else {
                $(this).append(tds);
            }
        }
    );
}
