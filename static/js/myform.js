function web_submit() {
    var params = $('#form_web').serialize();

    $.ajax({
        url: '/webupdate',
        type: 'POST',
        async: true,
        data: params,
        // dataType: 'json',
        success: function (data, textStatus) {
            console.log(data);
            data.filelist.forEach(function (value, index, array) {
                // $("#modal_body").append("<li>" + value + "</li>");
                $("#ul_modal").append("<li>" + value + "</li>");
            });
            $('#mymodal').modal('show')
        }
    })
}

$(document).ready(function () {
    $('.webdis').attr("disabled", "disabled");
    // $('.soadis').attr("disabled", "disabled");
    $('#web_select_app').change(function () {
        var selectText = $('#web_select_app').find("option:selected").val();
        if (selectText) {
            if ($('#web_txtarea_after').val()) {
                $(".webdis").removeAttr("disabled")
            }
            $('#web_txtarea_before').removeAttr("disabled");
            $('#web_input_app').val(selectText);
            $('#web_input_app').removeAttr('disabled');
            format_web();
        } else {
            $('.webdis').attr("disabled", "disabled");
            $('#web_input_app').val(selectText);
        }
    });

    // modal close
    $("#mymodal").on('hidden.bs.modal', function () {
        $("#ul_modal li").remove();
    });

    $("#modal_btn").click(function () {
        $("#isupdate").val("1");
        web_submit();
    })
});

function format_soa() {
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


function format_web() {
    var txtr_before = document.getElementById('web_txtarea_before');
    var txtr_after = document.getElementById('web_txtarea_after');
    var filelist = txtr_before.value;
    if (filelist.length == 0) {
        // alert('no lines');
        $("#web_txtarea_after").val('');
        $("#web_div_after").hide();
        $(".weblast").attr("disabled", "disabled");
        return 11;
    }

    filelist = filelist.replace(/\\/g, '/');
    filelist = filelist.replace(/\n(\n)*( )*(\n)*\n/g, '\n');
    filelist = filelist.replace(/\.java/g, '\.class');
    filelist = filelist.replace(/.*?src\/main\/(java|resources)\//g, 'WEB-INF/classes/');
    filelist = filelist.replace(/.*?src\/main\/webapp\//g, '');
    filelist = filelist.replace(/(^com\/|^.*?\/com\/)/gm, 'WEB-INF/classes/com/');

    app = $('#web_select_app').find("option:selected").val();
    // alert(app);
    if (app) {
        re_app = new RegExp("^.*?" + app + "/", "gm");
        filelist = filelist.replace(re_app, '')
    }

    if (/\.class$/gm.test(filelist)) {
        $("#web_reboot").prop('checked', true)
    } else {
        $("#web_noreboot").prop('checked', true)
    }

    row_num = filelist.split('\n').length;
    if (row_num > 8) {
        row_num = 8
    }

    txtr_after.value = filelist;
    txtr_before.rows = row_num;
    txtr_after.rows = row_num;

    $("#web_div_after").show();
    // $("#web_div_after").attr("readonly", "readonly");
    $(".webdis").removeAttr("disabled")
}

function web_select() {
    var select = document.getElementById('web_select_app');
    var app = select.options[select.selectedIndex].value;
}