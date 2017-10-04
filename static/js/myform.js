function submit2() {
    var filelist = document.getElementById('input_list').value;
    filelist = filelist.replace(/\\/g, '/');
    filelist = filelist.replace(/\.java/g, '\.class');

    document.getElementById('parsed_list').value = filelist;
    $.ajax({
        url: '/test',
        type: 'POST',
        async: true,

        data: {
            filelist: filelist
        },

        dataType: 'json',

        success: function (data, textStatus, jqXHR) {
            console.log(data);
            console.log(testStatus);
            console.log(jqXHR);
        }
    })
}

$(document).ready(function () {
    $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {
        var protype = $(e.target).text();
        $.get('applist', {'protype': protype}, function (res) {
            alert(res);
        })
    })
});

function format() {
    var txtr_before = document.getElementById('soa_txtarea_before');
    var txtr_after = document.getElementById('soa_txtarea_after');
    var filelist = txtr_before.value;
    if (filelist.length == 0) {
        // alert('no lines');
        $("#soa_div_after").hide();
        return 11;
    }

    filelist = filelist.replace(/\\/g, '/');
    filelist = filelist.replace(/\.java/g, '\.class');

    row_num = filelist.split('\n').length;
    if (row_num > 8) {
        row_num = 8
    }

    txtr_after.value = filelist;
    txtr_before.rows = row_num;
    txtr_after.rows = row_num;

    $("#soa_div_after").show();
}